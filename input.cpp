int main(int argc, char* argv[])
{
	int returnType;
	
	do
	{
		Game game(argc, argv);
		returnType = game.Run();

	} while (returnType == 1);

	return 0;
}