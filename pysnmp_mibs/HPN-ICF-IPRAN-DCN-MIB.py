_K='hpnicfIpRanDcnDeviceMac'
_J='hpnicfIpRanDcnDeviceType'
_I='hpnicfIpRanDcnCompanyName'
_H='Integer32'
_G='hpnicfIpRanDcnNeInfoNeIp'
_F='hpnicfIpRanDcnNeInfoNeIpType'
_E='hpnicfIpRanDcnNeInfoNeId'
_D='DisplayString'
_C='HPN-ICF-IPRAN-DCN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfCommon,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
hpnicfIpRanDcn=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,152))
if mibBuilder.loadTexts:hpnicfIpRanDcn.setRevisions(('2013-07-24 00:00',))
class HpnicfIpRanNeId(TextualConvention,OctetString):status=_A;displayHint='1d.1d.1d.1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_HpnicfIpRanDcnMIB_ObjectIdentity=ObjectIdentity
hpnicfIpRanDcnMIB=_HpnicfIpRanDcnMIB_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,152,1))
_HpnicfIpRanDcnObjects_ObjectIdentity=ObjectIdentity
hpnicfIpRanDcnObjects=_HpnicfIpRanDcnObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1))
_HpnicfIpRanDcnInfoObject_ObjectIdentity=ObjectIdentity
hpnicfIpRanDcnInfoObject=_HpnicfIpRanDcnInfoObject_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,1))
_HpnicfIpRanDcnNeId_Type=HpnicfIpRanNeId
_HpnicfIpRanDcnNeId_Object=MibScalar
hpnicfIpRanDcnNeId=_HpnicfIpRanDcnNeId_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,1,1),_HpnicfIpRanDcnNeId_Type())
hpnicfIpRanDcnNeId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeId.setStatus(_A)
_HpnicfIpRanDcnNeIpType_Type=InetAddressType
_HpnicfIpRanDcnNeIpType_Object=MibScalar
hpnicfIpRanDcnNeIpType=_HpnicfIpRanDcnNeIpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,1,2),_HpnicfIpRanDcnNeIpType_Type())
hpnicfIpRanDcnNeIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeIpType.setStatus(_A)
_HpnicfIpRanDcnNeIp_Type=InetAddress
_HpnicfIpRanDcnNeIp_Object=MibScalar
hpnicfIpRanDcnNeIp=_HpnicfIpRanDcnNeIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,1,3),_HpnicfIpRanDcnNeIp_Type())
hpnicfIpRanDcnNeIp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeIp.setStatus(_A)
_HpnicfIpRanDcnMask_Type=InetAddress
_HpnicfIpRanDcnMask_Object=MibScalar
hpnicfIpRanDcnMask=_HpnicfIpRanDcnMask_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,1,4),_HpnicfIpRanDcnMask_Type())
hpnicfIpRanDcnMask.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnMask.setStatus(_A)
_HpnicfIpRanDcnNeInfoTable_Object=MibTable
hpnicfIpRanDcnNeInfoTable=_HpnicfIpRanDcnNeInfoTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,2))
if mibBuilder.loadTexts:hpnicfIpRanDcnNeInfoTable.setStatus(_A)
_HpnicfIpRanDcnNeInfoEntry_Object=MibTableRow
hpnicfIpRanDcnNeInfoEntry=_HpnicfIpRanDcnNeInfoEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,2,1))
hpnicfIpRanDcnNeInfoEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:hpnicfIpRanDcnNeInfoEntry.setStatus(_A)
_HpnicfIpRanDcnNeInfoNeId_Type=HpnicfIpRanNeId
_HpnicfIpRanDcnNeInfoNeId_Object=MibTableColumn
hpnicfIpRanDcnNeInfoNeId=_HpnicfIpRanDcnNeInfoNeId_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,2,1,1),_HpnicfIpRanDcnNeInfoNeId_Type())
hpnicfIpRanDcnNeInfoNeId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeInfoNeId.setStatus(_A)
_HpnicfIpRanDcnNeInfoNeIpType_Type=InetAddressType
_HpnicfIpRanDcnNeInfoNeIpType_Object=MibTableColumn
hpnicfIpRanDcnNeInfoNeIpType=_HpnicfIpRanDcnNeInfoNeIpType_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,2,1,2),_HpnicfIpRanDcnNeInfoNeIpType_Type())
hpnicfIpRanDcnNeInfoNeIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeInfoNeIpType.setStatus(_A)
_HpnicfIpRanDcnNeInfoNeIp_Type=InetAddress
_HpnicfIpRanDcnNeInfoNeIp_Object=MibTableColumn
hpnicfIpRanDcnNeInfoNeIp=_HpnicfIpRanDcnNeInfoNeIp_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,2,1,3),_HpnicfIpRanDcnNeInfoNeIp_Type())
hpnicfIpRanDcnNeInfoNeIp.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeInfoNeIp.setStatus(_A)
_HpnicfIpRanDcnNeInfoMetric_Type=Integer32
_HpnicfIpRanDcnNeInfoMetric_Object=MibTableColumn
hpnicfIpRanDcnNeInfoMetric=_HpnicfIpRanDcnNeInfoMetric_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,2,1,4),_HpnicfIpRanDcnNeInfoMetric_Type())
hpnicfIpRanDcnNeInfoMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeInfoMetric.setStatus(_A)
class _HpnicfIpRanDcnNeInfoDeviceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIpRanDcnNeInfoDeviceType_Type.__name__=_D
_HpnicfIpRanDcnNeInfoDeviceType_Object=MibTableColumn
hpnicfIpRanDcnNeInfoDeviceType=_HpnicfIpRanDcnNeInfoDeviceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,1,2,1,5),_HpnicfIpRanDcnNeInfoDeviceType_Type())
hpnicfIpRanDcnNeInfoDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeInfoDeviceType.setStatus(_A)
_HpnicfIpRanDcnTrapObjects_ObjectIdentity=ObjectIdentity
hpnicfIpRanDcnTrapObjects=_HpnicfIpRanDcnTrapObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,152,1,2))
_HpnicfIpRanDcnNeNumber_Type=Integer32
_HpnicfIpRanDcnNeNumber_Object=MibScalar
hpnicfIpRanDcnNeNumber=_HpnicfIpRanDcnNeNumber_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,2,1),_HpnicfIpRanDcnNeNumber_Type())
hpnicfIpRanDcnNeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeNumber.setStatus(_A)
class _HpnicfIpRanDcnNeChangeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_HpnicfIpRanDcnNeChangeMode_Type.__name__=_H
_HpnicfIpRanDcnNeChangeMode_Object=MibScalar
hpnicfIpRanDcnNeChangeMode=_HpnicfIpRanDcnNeChangeMode_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,2,2),_HpnicfIpRanDcnNeChangeMode_Type())
hpnicfIpRanDcnNeChangeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnNeChangeMode.setStatus(_A)
class _HpnicfIpRanDcnCompanyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIpRanDcnCompanyName_Type.__name__=_D
_HpnicfIpRanDcnCompanyName_Object=MibScalar
hpnicfIpRanDcnCompanyName=_HpnicfIpRanDcnCompanyName_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,2,3),_HpnicfIpRanDcnCompanyName_Type())
hpnicfIpRanDcnCompanyName.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnCompanyName.setStatus(_A)
class _HpnicfIpRanDcnDeviceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_HpnicfIpRanDcnDeviceType_Type.__name__=_D
_HpnicfIpRanDcnDeviceType_Object=MibScalar
hpnicfIpRanDcnDeviceType=_HpnicfIpRanDcnDeviceType_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,2,4),_HpnicfIpRanDcnDeviceType_Type())
hpnicfIpRanDcnDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnDeviceType.setStatus(_A)
_HpnicfIpRanDcnDeviceMac_Type=MacAddress
_HpnicfIpRanDcnDeviceMac_Object=MibScalar
hpnicfIpRanDcnDeviceMac=_HpnicfIpRanDcnDeviceMac_Object((1,3,6,1,4,1,11,2,14,11,15,2,152,1,2,5),_HpnicfIpRanDcnDeviceMac_Type())
hpnicfIpRanDcnDeviceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfIpRanDcnDeviceMac.setStatus(_A)
_HpnicfIpRanDcnTraps_ObjectIdentity=ObjectIdentity
hpnicfIpRanDcnTraps=_HpnicfIpRanDcnTraps_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,152,1,3))
_HpnicfIpRanDcnTrapsPrefix_ObjectIdentity=ObjectIdentity
hpnicfIpRanDcnTrapsPrefix=_HpnicfIpRanDcnTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,152,1,3,0))
hpnicfIpRanDcnNeOnline=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,152,1,3,0,1))
hpnicfIpRanDcnNeOnline.setObjects(*((_C,_E),(_C,_F),(_C,_G),(_C,_I),(_C,_J),(_C,_K)))
if mibBuilder.loadTexts:hpnicfIpRanDcnNeOnline.setStatus(_A)
hpnicfIpRanDcnNeOffline=NotificationType((1,3,6,1,4,1,11,2,14,11,15,2,152,1,3,0,2))
hpnicfIpRanDcnNeOffline.setObjects(*((_C,_E),(_C,_F),(_C,_G)))
if mibBuilder.loadTexts:hpnicfIpRanDcnNeOffline.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'HpnicfIpRanNeId':HpnicfIpRanNeId,'hpnicfIpRanDcn':hpnicfIpRanDcn,'hpnicfIpRanDcnMIB':hpnicfIpRanDcnMIB,'hpnicfIpRanDcnObjects':hpnicfIpRanDcnObjects,'hpnicfIpRanDcnInfoObject':hpnicfIpRanDcnInfoObject,'hpnicfIpRanDcnNeId':hpnicfIpRanDcnNeId,'hpnicfIpRanDcnNeIpType':hpnicfIpRanDcnNeIpType,'hpnicfIpRanDcnNeIp':hpnicfIpRanDcnNeIp,'hpnicfIpRanDcnMask':hpnicfIpRanDcnMask,'hpnicfIpRanDcnNeInfoTable':hpnicfIpRanDcnNeInfoTable,'hpnicfIpRanDcnNeInfoEntry':hpnicfIpRanDcnNeInfoEntry,_E:hpnicfIpRanDcnNeInfoNeId,_F:hpnicfIpRanDcnNeInfoNeIpType,_G:hpnicfIpRanDcnNeInfoNeIp,'hpnicfIpRanDcnNeInfoMetric':hpnicfIpRanDcnNeInfoMetric,'hpnicfIpRanDcnNeInfoDeviceType':hpnicfIpRanDcnNeInfoDeviceType,'hpnicfIpRanDcnTrapObjects':hpnicfIpRanDcnTrapObjects,'hpnicfIpRanDcnNeNumber':hpnicfIpRanDcnNeNumber,'hpnicfIpRanDcnNeChangeMode':hpnicfIpRanDcnNeChangeMode,_I:hpnicfIpRanDcnCompanyName,_J:hpnicfIpRanDcnDeviceType,_K:hpnicfIpRanDcnDeviceMac,'hpnicfIpRanDcnTraps':hpnicfIpRanDcnTraps,'hpnicfIpRanDcnTrapsPrefix':hpnicfIpRanDcnTrapsPrefix,'hpnicfIpRanDcnNeOnline':hpnicfIpRanDcnNeOnline,'hpnicfIpRanDcnNeOffline':hpnicfIpRanDcnNeOffline})