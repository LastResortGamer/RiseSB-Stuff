import os

def Console():
    guilds = len(Rise.guilds)
    print(f'''{Fore.WHITE}
{Fore.WHITE}     {Fore.BLUE}██████╗{Fore.WHITE}  {Fore.RED}█████╗{Fore.WHITE}  {Fore.YELLOW}█████╗{Fore.WHITE}  {Fore.BLUE}██████╗{Fore.WHITE} {Fore.GREEN}██╗{Fore.WHITE}     {Fore.RED}███████╗{Fore.WHITE}  ██████╗  █████╗ ████████╗    
{Fore.WHITE}    {Fore.BLUE}██╔════╝{Fore.WHITE} {Fore.RED}██╔══██╗{Fore.YELLOW}██╔══██╗{Fore.BLUE}██╔════╝{Fore.WHITE} {Fore.GREEN}██║{Fore.WHITE}     {Fore.RED}██╔════╝{Fore.WHITE}  ██╔══██╗██╔══██╗╚══██╔══╝    
{Fore.WHITE}    {Fore.BLUE}██║{Fore.WHITE}  {Fore.BLUE}██╗{Fore.WHITE} {Fore.RED}██║{Fore.WHITE}  {Fore.RED}██║{Fore.YELLOW}██║{Fore.WHITE}  {Fore.YELLOW}██║{Fore.BLUE}██║{Fore.WHITE}  {Fore.BLUE}██╗{Fore.WHITE} {Fore.GREEN}██║{Fore.WHITE}     {Fore.RED}█████╗{Fore.WHITE}    ██████╦╝██║  ██║   ██║       
{Fore.WHITE}    {Fore.BLUE}██║{Fore.WHITE}  {Fore.BLUE}╚██╗{Fore.RED}██║{Fore.WHITE}  {Fore.RED}██║{Fore.YELLOW}██║{Fore.WHITE}  {Fore.YELLOW}██║{Fore.BLUE}██║{Fore.WHITE}  {Fore.BLUE}╚██╗{Fore.GREEN}██║{Fore.WHITE}     {Fore.RED}██╔══╝{Fore.WHITE}    ██╔══██╗██║  ██║   ██║       
{Fore.WHITE}    {Fore.BLUE}╚██████╔╝{Fore.RED}╚█████╔╝{Fore.YELLOW}╚█████╔╝{Fore.BLUE}╚██████╔╝{Fore.GREEN}███████╗{Fore.RED}███████╗{Fore.WHITE}  ██████╦╝╚█████╔╝   ██║       
{Fore.WHITE}     {Fore.BLUE}╚═════╝{Fore.WHITE}  {Fore.RED}╚════╝{Fore.WHITE}  {Fore.YELLOW}╚════╝{Fore.WHITE}  {Fore.BLUE}╚═════╝{Fore.WHITE} {Fore.GREEN}╚══════╝{Fore.RED}╚══════╝{Fore.WHITE}  ╚═════╝  ╚════╝    ╚═╝       
                                Don't Be Evil
                                        Use RiseSB
{Fore.RESET} ''')
    print(f'{Fore.LIGHTRED_EX}' 'Connected: ' + f'{Fore.WHITE}' + f'{Rise.user.name}' + f'{Fore.WHITE}' + '#' + f'{Fore.WHITE}' + f'{Rise.user.discriminator}' 
    + f'{Fore.LIGHTRED_EX}' ' Prefix: ' + f'{Fore.WHITE}' + '[' + f'{Fore.WHITE}' + f'{prefix}' + f'{Fore.WHITE}' + ']'
    + f'{Fore.LIGHTRED_EX}' ' Servers: ' + f'{Fore.WHITE}' + f'{guilds}'  )
    print(f'{Fore.WHITE}' '═' * os.get_terminal_size().columns)
    print(f'{Fore.LIGHTRED_EX}' 'Hint: Type' + f'{Fore.WHITE}' ' help ' + f'{Fore.LIGHTRED_EX}' 'in console to see all console commands.' )

os.system('mode con: cols=85 lines=25')

    
Console()
