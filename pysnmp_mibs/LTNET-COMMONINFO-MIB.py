_E='optional'
_D='OctetString'
_C='Integer32'
_B='mandatory'
_A='read-write'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_D,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ltnetRoot,=mibBuilder.importSymbols('LTNET-ROOT','ltnetRoot')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_LtnetCommonInfoGroup_ObjectIdentity=ObjectIdentity
ltnetCommonInfoGroup=_LtnetCommonInfoGroup_ObjectIdentity((1,3,6,1,4,1,33826,3))
_LtnetIpSimpleInfo_ObjectIdentity=ObjectIdentity
ltnetIpSimpleInfo=_LtnetIpSimpleInfo_ObjectIdentity((1,3,6,1,4,1,33826,3,1))
_LtnetIpNetAddress_Type=IpAddress
_LtnetIpNetAddress_Object=MibScalar
ltnetIpNetAddress=_LtnetIpNetAddress_Object((1,3,6,1,4,1,33826,3,1,1),_LtnetIpNetAddress_Type())
ltnetIpNetAddress.setMaxAccess(_A)
if mibBuilder.loadTexts:ltnetIpNetAddress.setStatus(_B)
class _LtnetIpMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_LtnetIpMask_Type.__name__=_C
_LtnetIpMask_Object=MibScalar
ltnetIpMask=_LtnetIpMask_Object((1,3,6,1,4,1,33826,3,1,2),_LtnetIpMask_Type())
ltnetIpMask.setMaxAccess(_A)
if mibBuilder.loadTexts:ltnetIpMask.setStatus(_B)
_LtnetIpDefaultGateway_Type=IpAddress
_LtnetIpDefaultGateway_Object=MibScalar
ltnetIpDefaultGateway=_LtnetIpDefaultGateway_Object((1,3,6,1,4,1,33826,3,1,3),_LtnetIpDefaultGateway_Type())
ltnetIpDefaultGateway.setMaxAccess(_A)
if mibBuilder.loadTexts:ltnetIpDefaultGateway.setStatus(_B)
_LtnetIpDns_Type=IpAddress
_LtnetIpDns_Object=MibScalar
ltnetIpDns=_LtnetIpDns_Object((1,3,6,1,4,1,33826,3,1,4),_LtnetIpDns_Type())
ltnetIpDns.setMaxAccess(_A)
if mibBuilder.loadTexts:ltnetIpDns.setStatus(_E)
_LtnetIpPhysicalAddress_Type=OctetString
_LtnetIpPhysicalAddress_Object=MibScalar
ltnetIpPhysicalAddress=_LtnetIpPhysicalAddress_Object((1,3,6,1,4,1,33826,3,1,5),_LtnetIpPhysicalAddress_Type())
ltnetIpPhysicalAddress.setMaxAccess('read-only')
if mibBuilder.loadTexts:ltnetIpPhysicalAddress.setStatus(_B)
_LtnetSubJoinedInfo_ObjectIdentity=ObjectIdentity
ltnetSubJoinedInfo=_LtnetSubJoinedInfo_ObjectIdentity((1,3,6,1,4,1,33826,3,4))
class _LtnetCommIdentifyNum_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,10))
_LtnetCommIdentifyNum_Type.__name__=_D
_LtnetCommIdentifyNum_Object=MibScalar
ltnetCommIdentifyNum=_LtnetCommIdentifyNum_Object((1,3,6,1,4,1,33826,3,4,1),_LtnetCommIdentifyNum_Type())
ltnetCommIdentifyNum.setMaxAccess(_A)
if mibBuilder.loadTexts:ltnetCommIdentifyNum.setStatus(_E)
_LtnetCommonTime_Type=Integer32
_LtnetCommonTime_Object=MibScalar
ltnetCommonTime=_LtnetCommonTime_Object((1,3,6,1,4,1,33826,3,4,2),_LtnetCommonTime_Type())
ltnetCommonTime.setMaxAccess(_A)
if mibBuilder.loadTexts:ltnetCommonTime.setStatus(_B)
class _LtnetAlarmDelayTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,600))
_LtnetAlarmDelayTime_Type.__name__=_C
_LtnetAlarmDelayTime_Object=MibScalar
ltnetAlarmDelayTime=_LtnetAlarmDelayTime_Object((1,3,6,1,4,1,33826,3,4,3),_LtnetAlarmDelayTime_Type())
ltnetAlarmDelayTime.setMaxAccess(_A)
if mibBuilder.loadTexts:ltnetAlarmDelayTime.setStatus(_B)
mibBuilder.exportSymbols('LTNET-COMMONINFO-MIB',**{'ltnetCommonInfoGroup':ltnetCommonInfoGroup,'ltnetIpSimpleInfo':ltnetIpSimpleInfo,'ltnetIpNetAddress':ltnetIpNetAddress,'ltnetIpMask':ltnetIpMask,'ltnetIpDefaultGateway':ltnetIpDefaultGateway,'ltnetIpDns':ltnetIpDns,'ltnetIpPhysicalAddress':ltnetIpPhysicalAddress,'ltnetSubJoinedInfo':ltnetSubJoinedInfo,'ltnetCommIdentifyNum':ltnetCommIdentifyNum,'ltnetCommonTime':ltnetCommonTime,'ltnetAlarmDelayTime':ltnetAlarmDelayTime})