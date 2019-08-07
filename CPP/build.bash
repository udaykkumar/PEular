#!/bin/bash
set -e


build ()
{
    if [ -f "CMakeLists.txt" ];
    then
        rm -rf build;
        mkdir build;
        pushd build;
        cmake ..
        make -j all
        popd

    elif [ -f "Makefile" ];
	then
    	make
    else
    	printf "No Make in $(PWD) Fix This .. \n"
    	exit
	fi	
}


run () 
{
	for testexec in $(find ./ -name "test.debug");
	do
		./${testexec} > /dev/null 2>&1 
	done

}


clean()
{
	if [ -f "Makefile" ];
	then
    	make clean
    else
    	printf "No Make in $(PWD) Fix This .. \n"
    	exit
	fi		
}

dist_clean()
{
	clean;
	printf "Cleaning deps\n";
    rm -rf deps
    rm -rf downloads
    
}

stage()
{
	if [ -f "Makefile" ];
	then
    	make stage
    else
    	printf "No Make in $(PWD) Fix This .. \n"
    	exit
	fi		
}

all()
{
	printf "\n\nCleaning ..\n\n"
	clean

	printf "\n\nInstalling dependency ..\n\n"
	install_deps

	printf "\n\nBuild .. stage .. test .. run ...\n\n"
    build
}

install_deps()
{


	local DEPENDENCY_BASE="./deps"
	local DEPENCENCY_REPO="./downloads"
	local BOOST="boost_1_68_0"
	local BOOST_PACKAGE="${BOOST}.tar.bz2"

	if [ ! -f "${DEPENCENCY_REPO}/${BOOST_PACKAGE}" ];
	then
		printf "\t\t[INSTALL_DEPS] ... recreate ${DEPENCENCY_REPO} ...\n"
		rm -rf ${DEPENCENCY_REPO}; mkdir -p ${DEPENCENCY_REPO}

		cd ${DEPENCENCY_REPO}
		printf "\t\t[INSTALL_DEPS] ... Download ${BOOST} ...\n"
		wget https://dl.bintray.com/boostorg/release/1.68.0/source/boost_1_68_0.tar.bz2 
		if [ ! -f "${BOOST_PACKAGE}" ];
		then
			printf "\t\t[INSTALL_DEPS] ... ${BOOST} Doesnot Exist in ${DEPENCENCY_REPO}...\n"
			printf "\t\t[INSTALL_DEPS] ... exiting ...\n"
			exit;
		fi
		cd ..
	else
		printf "\t\t[INSTALL_DEPS] ... ${BOOST_PACKAGE} Exists in ${DEPENCENCY_REPO}...\n"
	fi


	local boost_pack="${DEPENDENCY_BASE}/${BOOST_PACKAGE}" ;
	local boost_dir="${DEPENDENCY_BASE}/${BOOST}" ;
	
	rm -rf  "${DEPENDENCY_BASE}" ; 	mkdir -p "${DEPENDENCY_BASE}" ; 
	cp -f  "${DEPENCENCY_REPO}"/* "${DEPENDENCY_BASE}"

	
	if [ -f "${boost_pack}" ];
	then
		printf "\t\t[INSTALL_DEPS] ... ${boost_pack} is in path ...\n"
	else
		printf "\t\t[INSTALL_DEPS] ... ${boost_pack} is not in path ...\n"
		printf "\t\t[INSTALL_DEPS] ... dependency error .. boost not found\n"
		exit;
	fi
	
	printf "\t\t[INSTALL_DEPS] ... extracting ${boost_pack} ... \n"
	tar --bzip2 -xf "${boost_pack}" -C "${DEPENDENCY_BASE}"
	printf "\t\t[INSTALL_DEPS] ... Remove Unused ${boost_pack} ... \n"
	rm -f "${boost_pack}"
	printf "\t\t[INSTALL_DEPS] ... Ready to Use ${boost_dir} ... \n"
	printf "\t\t[INSTALL_DEPS] ... BOOST_ROOT = ${boost_dir} ... \n"

	cd "${boost_dir}";
		./bootstrap.sh 
		./b2 --with-test
	cd -


}

case "$1" 	in

	"build")
		build
		;;

	"clean")
		clean
		;;

	"dist_clean")
		dist_clean
		;;
			
	"test")
		run
		;;

	"all")
		all
		;;

	"stage")
		stage
		;;

	"install_deps")
		install_deps
		;;

    "help")	
		printf "supplied Option is [$1] It did not match the usage\n\n"
		printf "Usage : $0 [ clean | build | test | stage | all ] \n\n"
		printf "Still Triggering the build anyway with all \n"
		printf "Wait for 5 seconds before we trigger build\n\n"
        ;;

        *)
		all
		;;
esac
