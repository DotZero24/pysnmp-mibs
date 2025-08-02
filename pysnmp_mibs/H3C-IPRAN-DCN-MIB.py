_K='h3cIpRanDcnDeviceMac'
_J='h3cIpRanDcnDeviceType'
_I='h3cIpRanDcnCompanyName'
_H='Integer32'
_G='h3cIpRanDcnNeInfoNeIp'
_F='h3cIpRanDcnNeInfoNeIpType'
_E='h3cIpRanDcnNeInfoNeId'
_D='DisplayString'
_C='H3C-IPRAN-DCN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
h3cCommon,=mibBuilder.importSymbols('HUAWEI-3COM-OID-MIB','h3cCommon')
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_H,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_D,'MacAddress','PhysAddress','TextualConvention')
h3cIpRanDcn=ModuleIdentity((1,3,6,1,4,1,2011,10,2,152))
if mibBuilder.loadTexts:h3cIpRanDcn.setRevisions(('2015-01-30 00:00','2013-07-24 00:00'))
class H3cIpRanNeId(TextualConvention,OctetString):status=_A;displayHint='1d.1d.1d.1d';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(4,4));fixedLength=4
_H3cIpRanDcnMIB_ObjectIdentity=ObjectIdentity
h3cIpRanDcnMIB=_H3cIpRanDcnMIB_ObjectIdentity((1,3,6,1,4,1,2011,10,2,152,1))
_H3cIpRanDcnObjects_ObjectIdentity=ObjectIdentity
h3cIpRanDcnObjects=_H3cIpRanDcnObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,152,1,1))
_H3cIpRanDcnInfoObject_ObjectIdentity=ObjectIdentity
h3cIpRanDcnInfoObject=_H3cIpRanDcnInfoObject_ObjectIdentity((1,3,6,1,4,1,2011,10,2,152,1,1,1))
_H3cIpRanDcnNeId_Type=H3cIpRanNeId
_H3cIpRanDcnNeId_Object=MibScalar
h3cIpRanDcnNeId=_H3cIpRanDcnNeId_Object((1,3,6,1,4,1,2011,10,2,152,1,1,1,1),_H3cIpRanDcnNeId_Type())
h3cIpRanDcnNeId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeId.setStatus(_A)
_H3cIpRanDcnNeIpType_Type=InetAddressType
_H3cIpRanDcnNeIpType_Object=MibScalar
h3cIpRanDcnNeIpType=_H3cIpRanDcnNeIpType_Object((1,3,6,1,4,1,2011,10,2,152,1,1,1,2),_H3cIpRanDcnNeIpType_Type())
h3cIpRanDcnNeIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeIpType.setStatus(_A)
_H3cIpRanDcnNeIp_Type=InetAddress
_H3cIpRanDcnNeIp_Object=MibScalar
h3cIpRanDcnNeIp=_H3cIpRanDcnNeIp_Object((1,3,6,1,4,1,2011,10,2,152,1,1,1,3),_H3cIpRanDcnNeIp_Type())
h3cIpRanDcnNeIp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeIp.setStatus(_A)
_H3cIpRanDcnMask_Type=InetAddress
_H3cIpRanDcnMask_Object=MibScalar
h3cIpRanDcnMask=_H3cIpRanDcnMask_Object((1,3,6,1,4,1,2011,10,2,152,1,1,1,4),_H3cIpRanDcnMask_Type())
h3cIpRanDcnMask.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnMask.setStatus(_A)
_H3cIpRanDcnMAC_Type=MacAddress
_H3cIpRanDcnMAC_Object=MibScalar
h3cIpRanDcnMAC=_H3cIpRanDcnMAC_Object((1,3,6,1,4,1,2011,10,2,152,1,1,1,5),_H3cIpRanDcnMAC_Type())
h3cIpRanDcnMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnMAC.setStatus(_A)
class _H3cIpRanDcnVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIpRanDcnVendor_Type.__name__=_D
_H3cIpRanDcnVendor_Object=MibScalar
h3cIpRanDcnVendor=_H3cIpRanDcnVendor_Object((1,3,6,1,4,1,2011,10,2,152,1,1,1,6),_H3cIpRanDcnVendor_Type())
h3cIpRanDcnVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnVendor.setStatus(_A)
_H3cIpRanDcnNeInfoTable_Object=MibTable
h3cIpRanDcnNeInfoTable=_H3cIpRanDcnNeInfoTable_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2))
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoTable.setStatus(_A)
_H3cIpRanDcnNeInfoEntry_Object=MibTableRow
h3cIpRanDcnNeInfoEntry=_H3cIpRanDcnNeInfoEntry_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2,1))
h3cIpRanDcnNeInfoEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoEntry.setStatus(_A)
_H3cIpRanDcnNeInfoNeId_Type=H3cIpRanNeId
_H3cIpRanDcnNeInfoNeId_Object=MibTableColumn
h3cIpRanDcnNeInfoNeId=_H3cIpRanDcnNeInfoNeId_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2,1,1),_H3cIpRanDcnNeInfoNeId_Type())
h3cIpRanDcnNeInfoNeId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoNeId.setStatus(_A)
_H3cIpRanDcnNeInfoNeIpType_Type=InetAddressType
_H3cIpRanDcnNeInfoNeIpType_Object=MibTableColumn
h3cIpRanDcnNeInfoNeIpType=_H3cIpRanDcnNeInfoNeIpType_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2,1,2),_H3cIpRanDcnNeInfoNeIpType_Type())
h3cIpRanDcnNeInfoNeIpType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoNeIpType.setStatus(_A)
_H3cIpRanDcnNeInfoNeIp_Type=InetAddress
_H3cIpRanDcnNeInfoNeIp_Object=MibTableColumn
h3cIpRanDcnNeInfoNeIp=_H3cIpRanDcnNeInfoNeIp_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2,1,3),_H3cIpRanDcnNeInfoNeIp_Type())
h3cIpRanDcnNeInfoNeIp.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoNeIp.setStatus(_A)
_H3cIpRanDcnNeInfoMetric_Type=Integer32
_H3cIpRanDcnNeInfoMetric_Object=MibTableColumn
h3cIpRanDcnNeInfoMetric=_H3cIpRanDcnNeInfoMetric_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2,1,4),_H3cIpRanDcnNeInfoMetric_Type())
h3cIpRanDcnNeInfoMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoMetric.setStatus(_A)
class _H3cIpRanDcnNeInfoDeviceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIpRanDcnNeInfoDeviceType_Type.__name__=_D
_H3cIpRanDcnNeInfoDeviceType_Object=MibTableColumn
h3cIpRanDcnNeInfoDeviceType=_H3cIpRanDcnNeInfoDeviceType_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2,1,5),_H3cIpRanDcnNeInfoDeviceType_Type())
h3cIpRanDcnNeInfoDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoDeviceType.setStatus(_A)
_H3cIpRanDcnNeInfoMAC_Type=MacAddress
_H3cIpRanDcnNeInfoMAC_Object=MibTableColumn
h3cIpRanDcnNeInfoMAC=_H3cIpRanDcnNeInfoMAC_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2,1,6),_H3cIpRanDcnNeInfoMAC_Type())
h3cIpRanDcnNeInfoMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoMAC.setStatus(_A)
class _H3cIpRanDcnNeInfoVendor_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIpRanDcnNeInfoVendor_Type.__name__=_D
_H3cIpRanDcnNeInfoVendor_Object=MibTableColumn
h3cIpRanDcnNeInfoVendor=_H3cIpRanDcnNeInfoVendor_Object((1,3,6,1,4,1,2011,10,2,152,1,1,2,1,7),_H3cIpRanDcnNeInfoVendor_Type())
h3cIpRanDcnNeInfoVendor.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeInfoVendor.setStatus(_A)
_H3cIpRanDcnTrapObjects_ObjectIdentity=ObjectIdentity
h3cIpRanDcnTrapObjects=_H3cIpRanDcnTrapObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,152,1,2))
_H3cIpRanDcnNeNumber_Type=Integer32
_H3cIpRanDcnNeNumber_Object=MibScalar
h3cIpRanDcnNeNumber=_H3cIpRanDcnNeNumber_Object((1,3,6,1,4,1,2011,10,2,152,1,2,1),_H3cIpRanDcnNeNumber_Type())
h3cIpRanDcnNeNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeNumber.setStatus(_A)
class _H3cIpRanDcnNeChangeMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('online',1),('offline',2)))
_H3cIpRanDcnNeChangeMode_Type.__name__=_H
_H3cIpRanDcnNeChangeMode_Object=MibScalar
h3cIpRanDcnNeChangeMode=_H3cIpRanDcnNeChangeMode_Object((1,3,6,1,4,1,2011,10,2,152,1,2,2),_H3cIpRanDcnNeChangeMode_Type())
h3cIpRanDcnNeChangeMode.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnNeChangeMode.setStatus(_A)
class _H3cIpRanDcnCompanyName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIpRanDcnCompanyName_Type.__name__=_D
_H3cIpRanDcnCompanyName_Object=MibScalar
h3cIpRanDcnCompanyName=_H3cIpRanDcnCompanyName_Object((1,3,6,1,4,1,2011,10,2,152,1,2,3),_H3cIpRanDcnCompanyName_Type())
h3cIpRanDcnCompanyName.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnCompanyName.setStatus(_A)
class _H3cIpRanDcnDeviceType_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H3cIpRanDcnDeviceType_Type.__name__=_D
_H3cIpRanDcnDeviceType_Object=MibScalar
h3cIpRanDcnDeviceType=_H3cIpRanDcnDeviceType_Object((1,3,6,1,4,1,2011,10,2,152,1,2,4),_H3cIpRanDcnDeviceType_Type())
h3cIpRanDcnDeviceType.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnDeviceType.setStatus(_A)
_H3cIpRanDcnDeviceMac_Type=MacAddress
_H3cIpRanDcnDeviceMac_Object=MibScalar
h3cIpRanDcnDeviceMac=_H3cIpRanDcnDeviceMac_Object((1,3,6,1,4,1,2011,10,2,152,1,2,5),_H3cIpRanDcnDeviceMac_Type())
h3cIpRanDcnDeviceMac.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cIpRanDcnDeviceMac.setStatus(_A)
_H3cIpRanDcnTraps_ObjectIdentity=ObjectIdentity
h3cIpRanDcnTraps=_H3cIpRanDcnTraps_ObjectIdentity((1,3,6,1,4,1,2011,10,2,152,1,3))
_H3cIpRanDcnTrapsPrefix_ObjectIdentity=ObjectIdentity
h3cIpRanDcnTrapsPrefix=_H3cIpRanDcnTrapsPrefix_ObjectIdentity((1,3,6,1,4,1,2011,10,2,152,1,3,0))
h3cIpRanDcnNeOnline=NotificationType((1,3,6,1,4,1,2011,10,2,152,1,3,0,1))
h3cIpRanDcnNeOnline.setObjects(*((_C,_E),(_C,_F),(_C,_G),(_C,_I),(_C,_J),(_C,_K)))
if mibBuilder.loadTexts:h3cIpRanDcnNeOnline.setStatus(_A)
h3cIpRanDcnNeOffline=NotificationType((1,3,6,1,4,1,2011,10,2,152,1,3,0,2))
h3cIpRanDcnNeOffline.setObjects(*((_C,_E),(_C,_F),(_C,_G)))
if mibBuilder.loadTexts:h3cIpRanDcnNeOffline.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'H3cIpRanNeId':H3cIpRanNeId,'h3cIpRanDcn':h3cIpRanDcn,'h3cIpRanDcnMIB':h3cIpRanDcnMIB,'h3cIpRanDcnObjects':h3cIpRanDcnObjects,'h3cIpRanDcnInfoObject':h3cIpRanDcnInfoObject,'h3cIpRanDcnNeId':h3cIpRanDcnNeId,'h3cIpRanDcnNeIpType':h3cIpRanDcnNeIpType,'h3cIpRanDcnNeIp':h3cIpRanDcnNeIp,'h3cIpRanDcnMask':h3cIpRanDcnMask,'h3cIpRanDcnMAC':h3cIpRanDcnMAC,'h3cIpRanDcnVendor':h3cIpRanDcnVendor,'h3cIpRanDcnNeInfoTable':h3cIpRanDcnNeInfoTable,'h3cIpRanDcnNeInfoEntry':h3cIpRanDcnNeInfoEntry,_E:h3cIpRanDcnNeInfoNeId,_F:h3cIpRanDcnNeInfoNeIpType,_G:h3cIpRanDcnNeInfoNeIp,'h3cIpRanDcnNeInfoMetric':h3cIpRanDcnNeInfoMetric,'h3cIpRanDcnNeInfoDeviceType':h3cIpRanDcnNeInfoDeviceType,'h3cIpRanDcnNeInfoMAC':h3cIpRanDcnNeInfoMAC,'h3cIpRanDcnNeInfoVendor':h3cIpRanDcnNeInfoVendor,'h3cIpRanDcnTrapObjects':h3cIpRanDcnTrapObjects,'h3cIpRanDcnNeNumber':h3cIpRanDcnNeNumber,'h3cIpRanDcnNeChangeMode':h3cIpRanDcnNeChangeMode,_I:h3cIpRanDcnCompanyName,_J:h3cIpRanDcnDeviceType,_K:h3cIpRanDcnDeviceMac,'h3cIpRanDcnTraps':h3cIpRanDcnTraps,'h3cIpRanDcnTrapsPrefix':h3cIpRanDcnTrapsPrefix,'h3cIpRanDcnNeOnline':h3cIpRanDcnNeOnline,'h3cIpRanDcnNeOffline':h3cIpRanDcnNeOffline})