_F='loginFailureAttempts'
_E='loginFailureIPAddress'
_D='loginFailureUser'
_C='not-accessible'
_B='AT-TTY-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
DisplayStringUnsized,modules=mibBuilder.importSymbols('AT-SMI-MIB','DisplayStringUnsized','modules')
ifIndex,=mibBuilder.importSymbols('IF-MIB','ifIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
tty=ModuleIdentity((1,3,6,1,4,1,207,8,4,4,4,36))
if mibBuilder.loadTexts:tty.setRevisions(('2006-06-28 12:22',))
_TtyTraps_ObjectIdentity=ObjectIdentity
ttyTraps=_TtyTraps_ObjectIdentity((1,3,6,1,4,1,207,8,4,4,4,36,100))
_LoginFailureUser_Type=DisplayString
_LoginFailureUser_Object=MibScalar
loginFailureUser=_LoginFailureUser_Object((1,3,6,1,4,1,207,8,4,4,4,36,100,1),_LoginFailureUser_Type())
loginFailureUser.setMaxAccess(_C)
if mibBuilder.loadTexts:loginFailureUser.setStatus(_A)
_LoginFailureIPAddress_Type=IpAddress
_LoginFailureIPAddress_Object=MibScalar
loginFailureIPAddress=_LoginFailureIPAddress_Object((1,3,6,1,4,1,207,8,4,4,4,36,100,2),_LoginFailureIPAddress_Type())
loginFailureIPAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:loginFailureIPAddress.setStatus(_A)
_LoginFailureAttempts_Type=Integer32
_LoginFailureAttempts_Object=MibScalar
loginFailureAttempts=_LoginFailureAttempts_Object((1,3,6,1,4,1,207,8,4,4,4,36,100,3),_LoginFailureAttempts_Type())
loginFailureAttempts.setMaxAccess(_C)
if mibBuilder.loadTexts:loginFailureAttempts.setStatus(_A)
loginFailureTrap=NotificationType((1,3,6,1,4,1,207,8,4,4,4,36,100,11))
loginFailureTrap.setObjects(*((_B,_D),(_B,_E),(_B,_F)))
if mibBuilder.loadTexts:loginFailureTrap.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'tty':tty,'ttyTraps':ttyTraps,_D:loginFailureUser,_E:loginFailureIPAddress,_F:loginFailureAttempts,'loginFailureTrap':loginFailureTrap})