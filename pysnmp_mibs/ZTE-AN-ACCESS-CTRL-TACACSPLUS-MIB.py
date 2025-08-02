_L='zxAnTacacsPlusServerGrpName'
_K='seconds'
_J='zxAnTacacsPlusServerPort'
_I='zxAnTacacsPlusServerIpAddress'
_H='zxAnTacacsPlusServerIpType'
_G='read-create'
_F='not-accessible'
_E='DisplayString'
_D='read-write'
_C='Integer32'
_B='ZTE-AN-ACCESS-CTRL-TACACSPLUS-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'PhysAddress','RowStatus','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnAccessCtrlTacacsplusMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,92))
if mibBuilder.loadTexts:zxAnAccessCtrlTacacsplusMib.setRevisions(('2012-11-07 10:00',))
_ZxAnTacacsPlusGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnTacacsPlusGlobalObjects=_ZxAnTacacsPlusGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,92,1))
class _ZxAnTacacsPlusEnable_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_ZxAnTacacsPlusEnable_Type.__name__=_C
_ZxAnTacacsPlusEnable_Object=MibScalar
zxAnTacacsPlusEnable=_ZxAnTacacsPlusEnable_Object((1,3,6,1,4,1,3902,1015,92,1,1),_ZxAnTacacsPlusEnable_Type())
zxAnTacacsPlusEnable.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnTacacsPlusEnable.setStatus(_A)
class _ZxAnTacacsPlusMaxPacketSize_Type(Integer32):defaultValue=1024;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1024,4096))
_ZxAnTacacsPlusMaxPacketSize_Type.__name__=_C
_ZxAnTacacsPlusMaxPacketSize_Object=MibScalar
zxAnTacacsPlusMaxPacketSize=_ZxAnTacacsPlusMaxPacketSize_Object((1,3,6,1,4,1,3902,1015,92,1,2),_ZxAnTacacsPlusMaxPacketSize_Type())
zxAnTacacsPlusMaxPacketSize.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnTacacsPlusMaxPacketSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnTacacsPlusMaxPacketSize.setUnits('bytes')
_ZxAnTacacsPlusServerObjects_ObjectIdentity=ObjectIdentity
zxAnTacacsPlusServerObjects=_ZxAnTacacsPlusServerObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,92,2))
_ZxAnTacacsPlusSvrGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnTacacsPlusSvrGlobalObjects=_ZxAnTacacsPlusSvrGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,92,2,1))
class _ZxAnTacacsPlusGlobalServerKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnTacacsPlusGlobalServerKey_Type.__name__=_E
_ZxAnTacacsPlusGlobalServerKey_Object=MibScalar
zxAnTacacsPlusGlobalServerKey=_ZxAnTacacsPlusGlobalServerKey_Object((1,3,6,1,4,1,3902,1015,92,2,1,1),_ZxAnTacacsPlusGlobalServerKey_Type())
zxAnTacacsPlusGlobalServerKey.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnTacacsPlusGlobalServerKey.setStatus(_A)
class _ZxAnTacacsPlusTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1000))
_ZxAnTacacsPlusTimeout_Type.__name__=_C
_ZxAnTacacsPlusTimeout_Object=MibScalar
zxAnTacacsPlusTimeout=_ZxAnTacacsPlusTimeout_Object((1,3,6,1,4,1,3902,1015,92,2,1,2),_ZxAnTacacsPlusTimeout_Type())
zxAnTacacsPlusTimeout.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnTacacsPlusTimeout.setStatus(_A)
if mibBuilder.loadTexts:zxAnTacacsPlusTimeout.setUnits(_K)
_ZxAnTacacsPlusServer_ObjectIdentity=ObjectIdentity
zxAnTacacsPlusServer=_ZxAnTacacsPlusServer_ObjectIdentity((1,3,6,1,4,1,3902,1015,92,2,2))
_ZxAnTacacsPlusServerTable_Object=MibTable
zxAnTacacsPlusServerTable=_ZxAnTacacsPlusServerTable_Object((1,3,6,1,4,1,3902,1015,92,2,2,2))
if mibBuilder.loadTexts:zxAnTacacsPlusServerTable.setStatus(_A)
_ZxAnTacacsPlusServerEntry_Object=MibTableRow
zxAnTacacsPlusServerEntry=_ZxAnTacacsPlusServerEntry_Object((1,3,6,1,4,1,3902,1015,92,2,2,2,1))
zxAnTacacsPlusServerEntry.setIndexNames((0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:zxAnTacacsPlusServerEntry.setStatus(_A)
_ZxAnTacacsPlusServerIpType_Type=InetAddressType
_ZxAnTacacsPlusServerIpType_Object=MibTableColumn
zxAnTacacsPlusServerIpType=_ZxAnTacacsPlusServerIpType_Object((1,3,6,1,4,1,3902,1015,92,2,2,2,1,1),_ZxAnTacacsPlusServerIpType_Type())
zxAnTacacsPlusServerIpType.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTacacsPlusServerIpType.setStatus(_A)
_ZxAnTacacsPlusServerIpAddress_Type=InetAddress
_ZxAnTacacsPlusServerIpAddress_Object=MibTableColumn
zxAnTacacsPlusServerIpAddress=_ZxAnTacacsPlusServerIpAddress_Object((1,3,6,1,4,1,3902,1015,92,2,2,2,1,2),_ZxAnTacacsPlusServerIpAddress_Type())
zxAnTacacsPlusServerIpAddress.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTacacsPlusServerIpAddress.setStatus(_A)
class _ZxAnTacacsPlusServerPort_Type(Integer32):defaultValue=49;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(49,49),ValueRangeConstraint(1025,65535))
_ZxAnTacacsPlusServerPort_Type.__name__=_C
_ZxAnTacacsPlusServerPort_Object=MibTableColumn
zxAnTacacsPlusServerPort=_ZxAnTacacsPlusServerPort_Object((1,3,6,1,4,1,3902,1015,92,2,2,2,1,3),_ZxAnTacacsPlusServerPort_Type())
zxAnTacacsPlusServerPort.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTacacsPlusServerPort.setStatus(_A)
class _ZxAnTacacsPlusServerKey_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnTacacsPlusServerKey_Type.__name__=_E
_ZxAnTacacsPlusServerKey_Object=MibTableColumn
zxAnTacacsPlusServerKey=_ZxAnTacacsPlusServerKey_Object((1,3,6,1,4,1,3902,1015,92,2,2,2,1,4),_ZxAnTacacsPlusServerKey_Type())
zxAnTacacsPlusServerKey.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnTacacsPlusServerKey.setStatus(_A)
class _ZxAnTacacsPlusServerTimeout_Type(Integer32):defaultValue=5;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1000))
_ZxAnTacacsPlusServerTimeout_Type.__name__=_C
_ZxAnTacacsPlusServerTimeout_Object=MibTableColumn
zxAnTacacsPlusServerTimeout=_ZxAnTacacsPlusServerTimeout_Object((1,3,6,1,4,1,3902,1015,92,2,2,2,1,5),_ZxAnTacacsPlusServerTimeout_Type())
zxAnTacacsPlusServerTimeout.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnTacacsPlusServerTimeout.setStatus(_A)
if mibBuilder.loadTexts:zxAnTacacsPlusServerTimeout.setUnits(_K)
_ZxAnTacacsPlusServerRowStatus_Type=RowStatus
_ZxAnTacacsPlusServerRowStatus_Object=MibTableColumn
zxAnTacacsPlusServerRowStatus=_ZxAnTacacsPlusServerRowStatus_Object((1,3,6,1,4,1,3902,1015,92,2,2,2,1,50),_ZxAnTacacsPlusServerRowStatus_Type())
zxAnTacacsPlusServerRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnTacacsPlusServerRowStatus.setStatus(_A)
_ZxAnTacacsPlusServerGroupTable_Object=MibTable
zxAnTacacsPlusServerGroupTable=_ZxAnTacacsPlusServerGroupTable_Object((1,3,6,1,4,1,3902,1015,92,2,2,3))
if mibBuilder.loadTexts:zxAnTacacsPlusServerGroupTable.setStatus(_A)
_ZxAnTacacsPlusServerGroupEntry_Object=MibTableRow
zxAnTacacsPlusServerGroupEntry=_ZxAnTacacsPlusServerGroupEntry_Object((1,3,6,1,4,1,3902,1015,92,2,2,3,1))
zxAnTacacsPlusServerGroupEntry.setIndexNames((0,_B,_L),(0,_B,_H),(0,_B,_I),(0,_B,_J))
if mibBuilder.loadTexts:zxAnTacacsPlusServerGroupEntry.setStatus(_A)
class _ZxAnTacacsPlusServerGrpName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnTacacsPlusServerGrpName_Type.__name__=_E
_ZxAnTacacsPlusServerGrpName_Object=MibTableColumn
zxAnTacacsPlusServerGrpName=_ZxAnTacacsPlusServerGrpName_Object((1,3,6,1,4,1,3902,1015,92,2,2,3,1,1),_ZxAnTacacsPlusServerGrpName_Type())
zxAnTacacsPlusServerGrpName.setMaxAccess(_F)
if mibBuilder.loadTexts:zxAnTacacsPlusServerGrpName.setStatus(_A)
_ZxAnTacacsPlusServerGrpRowStatus_Type=RowStatus
_ZxAnTacacsPlusServerGrpRowStatus_Object=MibTableColumn
zxAnTacacsPlusServerGrpRowStatus=_ZxAnTacacsPlusServerGrpRowStatus_Object((1,3,6,1,4,1,3902,1015,92,2,2,3,1,50),_ZxAnTacacsPlusServerGrpRowStatus_Type())
zxAnTacacsPlusServerGrpRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnTacacsPlusServerGrpRowStatus.setStatus(_A)
_ZxAnTacacsPlusClientObjects_ObjectIdentity=ObjectIdentity
zxAnTacacsPlusClientObjects=_ZxAnTacacsPlusClientObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,92,3))
_ZxAnTacacsPlusClntGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnTacacsPlusClntGlobalObjects=_ZxAnTacacsPlusClntGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,92,3,1))
_ZxAnTacacsPlusClientIpType_Type=InetAddressType
_ZxAnTacacsPlusClientIpType_Object=MibScalar
zxAnTacacsPlusClientIpType=_ZxAnTacacsPlusClientIpType_Object((1,3,6,1,4,1,3902,1015,92,3,1,1),_ZxAnTacacsPlusClientIpType_Type())
zxAnTacacsPlusClientIpType.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnTacacsPlusClientIpType.setStatus(_A)
_ZxAnTacacsPlusClientIpAddr_Type=InetAddress
_ZxAnTacacsPlusClientIpAddr_Object=MibScalar
zxAnTacacsPlusClientIpAddr=_ZxAnTacacsPlusClientIpAddr_Object((1,3,6,1,4,1,3902,1015,92,3,1,2),_ZxAnTacacsPlusClientIpAddr_Type())
zxAnTacacsPlusClientIpAddr.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnTacacsPlusClientIpAddr.setStatus(_A)
class _ZxAnTacacsPlusClientPort_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1025,65535))
_ZxAnTacacsPlusClientPort_Type.__name__=_C
_ZxAnTacacsPlusClientPort_Object=MibScalar
zxAnTacacsPlusClientPort=_ZxAnTacacsPlusClientPort_Object((1,3,6,1,4,1,3902,1015,92,3,1,3),_ZxAnTacacsPlusClientPort_Type())
zxAnTacacsPlusClientPort.setMaxAccess(_D)
if mibBuilder.loadTexts:zxAnTacacsPlusClientPort.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'zxAnAccessCtrlTacacsplusMib':zxAnAccessCtrlTacacsplusMib,'zxAnTacacsPlusGlobalObjects':zxAnTacacsPlusGlobalObjects,'zxAnTacacsPlusEnable':zxAnTacacsPlusEnable,'zxAnTacacsPlusMaxPacketSize':zxAnTacacsPlusMaxPacketSize,'zxAnTacacsPlusServerObjects':zxAnTacacsPlusServerObjects,'zxAnTacacsPlusSvrGlobalObjects':zxAnTacacsPlusSvrGlobalObjects,'zxAnTacacsPlusGlobalServerKey':zxAnTacacsPlusGlobalServerKey,'zxAnTacacsPlusTimeout':zxAnTacacsPlusTimeout,'zxAnTacacsPlusServer':zxAnTacacsPlusServer,'zxAnTacacsPlusServerTable':zxAnTacacsPlusServerTable,'zxAnTacacsPlusServerEntry':zxAnTacacsPlusServerEntry,_H:zxAnTacacsPlusServerIpType,_I:zxAnTacacsPlusServerIpAddress,_J:zxAnTacacsPlusServerPort,'zxAnTacacsPlusServerKey':zxAnTacacsPlusServerKey,'zxAnTacacsPlusServerTimeout':zxAnTacacsPlusServerTimeout,'zxAnTacacsPlusServerRowStatus':zxAnTacacsPlusServerRowStatus,'zxAnTacacsPlusServerGroupTable':zxAnTacacsPlusServerGroupTable,'zxAnTacacsPlusServerGroupEntry':zxAnTacacsPlusServerGroupEntry,_L:zxAnTacacsPlusServerGrpName,'zxAnTacacsPlusServerGrpRowStatus':zxAnTacacsPlusServerGrpRowStatus,'zxAnTacacsPlusClientObjects':zxAnTacacsPlusClientObjects,'zxAnTacacsPlusClntGlobalObjects':zxAnTacacsPlusClntGlobalObjects,'zxAnTacacsPlusClientIpType':zxAnTacacsPlusClientIpType,'zxAnTacacsPlusClientIpAddr':zxAnTacacsPlusClientIpAddr,'zxAnTacacsPlusClientPort':zxAnTacacsPlusClientPort})