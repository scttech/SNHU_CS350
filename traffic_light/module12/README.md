# Module 12: Cleanup and Enhancements

In this module we will take a look at some general cleanup to the code.

We will also briefly discuss ideas for expanding the traffic light project.

## Docker

The `docker-compose.yml` file repeated the database username, password, as well as some other fields between containers.
While our project is not that large, it still would be benefecial to consolidate these shared variables into a single
maintainable location.

In the [docker](./docker) directory we 