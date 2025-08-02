_G='telnetUserTerminal'
_F='GBNPlatformOAMTelnet-MIB'
_E='read-write'
_D='Integer32'
_C='DisplayString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
gbnPlatformOAM,=mibBuilder.importSymbols('GBNPlatformOAM-MIB','gbnPlatformOAM')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
snmpTraps,=mibBuilder.importSymbols('SNMPv2-MIB','snmpTraps')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_C,'MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
gbnPlatformOAMTelnet=ModuleIdentity((1,3,6,1,4,1,13464,1,2,1,1,15))
if mibBuilder.loadTexts:gbnPlatformOAMTelnet.setRevisions(('1913-04-16 00:00',))
class _TelnetState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),('disable',2)))
_TelnetState_Type.__name__=_D
_TelnetState_Object=MibScalar
telnetState=_TelnetState_Object((1,3,6,1,4,1,13464,1,2,1,1,15,1),_TelnetState_Type())
telnetState.setMaxAccess(_E)
if mibBuilder.loadTexts:telnetState.setStatus(_A)
class _TelnetUserLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,5))
_TelnetUserLimit_Type.__name__=_D
_TelnetUserLimit_Object=MibScalar
telnetUserLimit=_TelnetUserLimit_Object((1,3,6,1,4,1,13464,1,2,1,1,15,2),_TelnetUserLimit_Type())
telnetUserLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:telnetUserLimit.setStatus(_A)
_TelnetLoginUsers_Type=Counter32
_TelnetLoginUsers_Object=MibScalar
telnetLoginUsers=_TelnetLoginUsers_Object((1,3,6,1,4,1,13464,1,2,1,1,15,3),_TelnetLoginUsers_Type())
telnetLoginUsers.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetLoginUsers.setStatus(_A)
_TelnetUserTable_Object=MibTable
telnetUserTable=_TelnetUserTable_Object((1,3,6,1,4,1,13464,1,2,1,1,15,4))
if mibBuilder.loadTexts:telnetUserTable.setStatus(_A)
_TelnetUserEntry_Object=MibTableRow
telnetUserEntry=_TelnetUserEntry_Object((1,3,6,1,4,1,13464,1,2,1,1,15,4,1))
telnetUserEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:telnetUserEntry.setStatus(_A)
_TelnetUserTerminal_Type=Counter32
_TelnetUserTerminal_Object=MibTableColumn
telnetUserTerminal=_TelnetUserTerminal_Object((1,3,6,1,4,1,13464,1,2,1,1,15,4,1,1),_TelnetUserTerminal_Type())
telnetUserTerminal.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetUserTerminal.setStatus(_A)
class _TelnetUserAddrIp_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,64))
_TelnetUserAddrIp_Type.__name__=_C
_TelnetUserAddrIp_Object=MibTableColumn
telnetUserAddrIp=_TelnetUserAddrIp_Object((1,3,6,1,4,1,13464,1,2,1,1,15,4,1,2),_TelnetUserAddrIp_Type())
telnetUserAddrIp.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetUserAddrIp.setStatus(_A)
class _TelnetUserName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_TelnetUserName_Type.__name__=_C
_TelnetUserName_Object=MibTableColumn
telnetUserName=_TelnetUserName_Object((1,3,6,1,4,1,13464,1,2,1,1,15,4,1,3),_TelnetUserName_Type())
telnetUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetUserName.setStatus(_A)
class _TelnetUserLoginTime_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,100))
_TelnetUserLoginTime_Type.__name__=_C
_TelnetUserLoginTime_Object=MibTableColumn
telnetUserLoginTime=_TelnetUserLoginTime_Object((1,3,6,1,4,1,13464,1,2,1,1,15,4,1,4),_TelnetUserLoginTime_Type())
telnetUserLoginTime.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetUserLoginTime.setStatus(_A)
class _TelnetUserTransport_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_TelnetUserTransport_Type.__name__=_C
_TelnetUserTransport_Object=MibTableColumn
telnetUserTransport=_TelnetUserTransport_Object((1,3,6,1,4,1,13464,1,2,1,1,15,4,1,5),_TelnetUserTransport_Type())
telnetUserTransport.setMaxAccess(_B)
if mibBuilder.loadTexts:telnetUserTransport.setStatus(_A)
_TelnetUserRowStatus_Type=RowStatus
_TelnetUserRowStatus_Object=MibTableColumn
telnetUserRowStatus=_TelnetUserRowStatus_Object((1,3,6,1,4,1,13464,1,2,1,1,15,4,1,6),_TelnetUserRowStatus_Type())
telnetUserRowStatus.setMaxAccess(_E)
if mibBuilder.loadTexts:telnetUserRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'gbnPlatformOAMTelnet':gbnPlatformOAMTelnet,'telnetState':telnetState,'telnetUserLimit':telnetUserLimit,'telnetLoginUsers':telnetLoginUsers,'telnetUserTable':telnetUserTable,'telnetUserEntry':telnetUserEntry,_G:telnetUserTerminal,'telnetUserAddrIp':telnetUserAddrIp,'telnetUserName':telnetUserName,'telnetUserLoginTime':telnetUserLoginTime,'telnetUserTransport':telnetUserTransport,'telnetUserRowStatus':telnetUserRowStatus})