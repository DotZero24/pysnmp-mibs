_G='rlTelnetSessionId'
_F='NETGEAR-RADLAN-TELNET-MIB'
_E='DisplayString'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
rnd,=mibBuilder.importSymbols('NETGEAR-RADLAN-MIB','rnd')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','TextualConvention','TruthValue')
rlTelnet=ModuleIdentity((1,3,6,1,4,1,4526,17,58))
if mibBuilder.loadTexts:rlTelnet.setRevisions(('2008-11-24 00:00',))
_RlTelnetMibVersion_Type=Integer32
_RlTelnetMibVersion_Object=MibScalar
rlTelnetMibVersion=_RlTelnetMibVersion_Object((1,3,6,1,4,1,4526,17,58,1),_RlTelnetMibVersion_Type())
rlTelnetMibVersion.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTelnetMibVersion.setStatus(_A)
class _RlTelnetPassword_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,20))
_RlTelnetPassword_Type.__name__=_E
_RlTelnetPassword_Object=MibScalar
rlTelnetPassword=_RlTelnetPassword_Object((1,3,6,1,4,1,4526,17,58,2),_RlTelnetPassword_Type())
rlTelnetPassword.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTelnetPassword.setStatus(_A)
class _RlTelnetTimeout_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_RlTelnetTimeout_Type.__name__=_D
_RlTelnetTimeout_Object=MibScalar
rlTelnetTimeout=_RlTelnetTimeout_Object((1,3,6,1,4,1,4526,17,58,3),_RlTelnetTimeout_Type())
rlTelnetTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTelnetTimeout.setStatus(_A)
_RlTelnetUsersTable_Object=MibTable
rlTelnetUsersTable=_RlTelnetUsersTable_Object((1,3,6,1,4,1,4526,17,58,4))
if mibBuilder.loadTexts:rlTelnetUsersTable.setStatus(_A)
_RlTelnetUsersEntry_Object=MibTableRow
rlTelnetUsersEntry=_RlTelnetUsersEntry_Object((1,3,6,1,4,1,4526,17,58,4,1))
rlTelnetUsersEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:rlTelnetUsersEntry.setStatus(_A)
_RlTelnetSessionId_Type=Integer32
_RlTelnetSessionId_Object=MibTableColumn
rlTelnetSessionId=_RlTelnetSessionId_Object((1,3,6,1,4,1,4526,17,58,4,1,1),_RlTelnetSessionId_Type())
rlTelnetSessionId.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTelnetSessionId.setStatus(_A)
_RlTelnetSessionClientAddressType_Type=InetAddressType
_RlTelnetSessionClientAddressType_Object=MibTableColumn
rlTelnetSessionClientAddressType=_RlTelnetSessionClientAddressType_Object((1,3,6,1,4,1,4526,17,58,4,1,2),_RlTelnetSessionClientAddressType_Type())
rlTelnetSessionClientAddressType.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTelnetSessionClientAddressType.setStatus(_A)
_RlTelnetSessionClientAddress_Type=InetAddress
_RlTelnetSessionClientAddress_Object=MibTableColumn
rlTelnetSessionClientAddress=_RlTelnetSessionClientAddress_Object((1,3,6,1,4,1,4526,17,58,4,1,3),_RlTelnetSessionClientAddress_Type())
rlTelnetSessionClientAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTelnetSessionClientAddress.setStatus(_A)
_RlTelnetSessionLoginTime_Type=DisplayString
_RlTelnetSessionLoginTime_Object=MibTableColumn
rlTelnetSessionLoginTime=_RlTelnetSessionLoginTime_Object((1,3,6,1,4,1,4526,17,58,4,1,4),_RlTelnetSessionLoginTime_Type())
rlTelnetSessionLoginTime.setMaxAccess(_C)
if mibBuilder.loadTexts:rlTelnetSessionLoginTime.setStatus(_A)
class _RlTelnetSessionStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('connected',1),('disconnect',2)))
_RlTelnetSessionStatus_Type.__name__=_D
_RlTelnetSessionStatus_Object=MibTableColumn
rlTelnetSessionStatus=_RlTelnetSessionStatus_Object((1,3,6,1,4,1,4526,17,58,4,1,5),_RlTelnetSessionStatus_Type())
rlTelnetSessionStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTelnetSessionStatus.setStatus(_A)
_RlTelnetLoginBanner_Type=DisplayString
_RlTelnetLoginBanner_Object=MibScalar
rlTelnetLoginBanner=_RlTelnetLoginBanner_Object((1,3,6,1,4,1,4526,17,58,5),_RlTelnetLoginBanner_Type())
rlTelnetLoginBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTelnetLoginBanner.setStatus(_A)
_RlTelnetSecondLoginBanner_Type=DisplayString
_RlTelnetSecondLoginBanner_Object=MibScalar
rlTelnetSecondLoginBanner=_RlTelnetSecondLoginBanner_Object((1,3,6,1,4,1,4526,17,58,6),_RlTelnetSecondLoginBanner_Type())
rlTelnetSecondLoginBanner.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTelnetSecondLoginBanner.setStatus(_A)
_RlTelnetEnable_Type=TruthValue
_RlTelnetEnable_Object=MibScalar
rlTelnetEnable=_RlTelnetEnable_Object((1,3,6,1,4,1,4526,17,58,7),_RlTelnetEnable_Type())
rlTelnetEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rlTelnetEnable.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'rlTelnet':rlTelnet,'rlTelnetMibVersion':rlTelnetMibVersion,'rlTelnetPassword':rlTelnetPassword,'rlTelnetTimeout':rlTelnetTimeout,'rlTelnetUsersTable':rlTelnetUsersTable,'rlTelnetUsersEntry':rlTelnetUsersEntry,_G:rlTelnetSessionId,'rlTelnetSessionClientAddressType':rlTelnetSessionClientAddressType,'rlTelnetSessionClientAddress':rlTelnetSessionClientAddress,'rlTelnetSessionLoginTime':rlTelnetSessionLoginTime,'rlTelnetSessionStatus':rlTelnetSessionStatus,'rlTelnetLoginBanner':rlTelnetLoginBanner,'rlTelnetSecondLoginBanner':rlTelnetSecondLoginBanner,'rlTelnetEnable':rlTelnetEnable})