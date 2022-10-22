launch_dev_env:
	docker build					\
		--file Dockerfile.dev_env	\
		--tag dev_env				\
		.
	docker run						\
		--privileged				\
		--interactive				\
		--detach					\
		dev_env
		
