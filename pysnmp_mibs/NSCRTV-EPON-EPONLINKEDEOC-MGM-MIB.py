_J='ePortIndex'
_I='eCardIndex'
_H='eDeviceIndex'
_G='Integer32'
_F='not-accessible'
_E='NSCRTV-EPON-EPONLINKEDEOC-MGM-MIB'
_D='read-write'
_C='OctetString'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
AutoNegotiationTechAbility,EponAlarmCode,EponAlarmInstance,EponCardIndex,EponDeviceIndex,EponPortIndex,EponSeverityType,EponStats15MinRecordType,EponStats24HourRecordType,EponStatsThresholdType,TAddress,eponLinkedEoCManagementObjects=mibBuilder.importSymbols('NSCRTV-EPONEOC-EPON-MIB','AutoNegotiationTechAbility','EponAlarmCode','EponAlarmInstance','EponCardIndex','EponDeviceIndex','EponPortIndex','EponSeverityType','EponStats15MinRecordType','EponStats24HourRecordType','EponStatsThresholdType','TAddress','eponLinkedEoCManagementObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DateAndTime,DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TimeStamp,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DateAndTime','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TimeStamp','TruthValue')
_EocDevInfoTable_Object=MibTable
eocDevInfoTable=_EocDevInfoTable_Object((1,3,6,1,4,1,17409,2,3,11,1))
if mibBuilder.loadTexts:eocDevInfoTable.setStatus(_A)
_EocDevInfoEntry_Object=MibTableRow
eocDevInfoEntry=_EocDevInfoEntry_Object((1,3,6,1,4,1,17409,2,3,11,1,1))
eocDevInfoEntry.setIndexNames((0,_E,_H),(0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:eocDevInfoEntry.setStatus(_A)
_EDeviceIndex_Type=EponDeviceIndex
_EDeviceIndex_Object=MibTableColumn
eDeviceIndex=_EDeviceIndex_Object((1,3,6,1,4,1,17409,2,3,11,1,1,1),_EDeviceIndex_Type())
eDeviceIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eDeviceIndex.setStatus(_A)
_ECardIndex_Type=EponCardIndex
_ECardIndex_Object=MibTableColumn
eCardIndex=_ECardIndex_Object((1,3,6,1,4,1,17409,2,3,11,1,1,2),_ECardIndex_Type())
eCardIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:eCardIndex.setStatus(_A)
_EPortIndex_Type=EponPortIndex
_EPortIndex_Object=MibTableColumn
ePortIndex=_EPortIndex_Object((1,3,6,1,4,1,17409,2,3,11,1,1,3),_EPortIndex_Type())
ePortIndex.setMaxAccess(_F)
if mibBuilder.loadTexts:ePortIndex.setStatus(_A)
class _EocDeviceTechnologyProject_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EocDeviceTechnologyProject_Type.__name__=_C
_EocDeviceTechnologyProject_Object=MibTableColumn
eocDeviceTechnologyProject=_EocDeviceTechnologyProject_Object((1,3,6,1,4,1,17409,2,3,11,1,1,4),_EocDeviceTechnologyProject_Type())
eocDeviceTechnologyProject.setMaxAccess(_B)
if mibBuilder.loadTexts:eocDeviceTechnologyProject.setStatus(_A)
class _EocDeviceVendorName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EocDeviceVendorName_Type.__name__=_C
_EocDeviceVendorName_Object=MibTableColumn
eocDeviceVendorName=_EocDeviceVendorName_Object((1,3,6,1,4,1,17409,2,3,11,1,1,5),_EocDeviceVendorName_Type())
eocDeviceVendorName.setMaxAccess(_B)
if mibBuilder.loadTexts:eocDeviceVendorName.setStatus(_A)
class _EocDeviceProductType_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EocDeviceProductType_Type.__name__=_C
_EocDeviceProductType_Object=MibTableColumn
eocDeviceProductType=_EocDeviceProductType_Object((1,3,6,1,4,1,17409,2,3,11,1,1,6),_EocDeviceProductType_Type())
eocDeviceProductType.setMaxAccess(_B)
if mibBuilder.loadTexts:eocDeviceProductType.setStatus(_A)
class _EocDeviceSoftwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EocDeviceSoftwareVersion_Type.__name__=_C
_EocDeviceSoftwareVersion_Object=MibTableColumn
eocDeviceSoftwareVersion=_EocDeviceSoftwareVersion_Object((1,3,6,1,4,1,17409,2,3,11,1,1,7),_EocDeviceSoftwareVersion_Type())
eocDeviceSoftwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eocDeviceSoftwareVersion.setStatus(_A)
class _EocDeviceHardwareVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EocDeviceHardwareVersion_Type.__name__=_C
_EocDeviceHardwareVersion_Object=MibTableColumn
eocDeviceHardwareVersion=_EocDeviceHardwareVersion_Object((1,3,6,1,4,1,17409,2,3,11,1,1,8),_EocDeviceHardwareVersion_Type())
eocDeviceHardwareVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eocDeviceHardwareVersion.setStatus(_A)
class _EocSeriesNumber_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,64))
_EocSeriesNumber_Type.__name__=_C
_EocSeriesNumber_Object=MibTableColumn
eocSeriesNumber=_EocSeriesNumber_Object((1,3,6,1,4,1,17409,2,3,11,1,1,9),_EocSeriesNumber_Type())
eocSeriesNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:eocSeriesNumber.setStatus(_A)
_EocDeviceIpAddress_Type=IpAddress
_EocDeviceIpAddress_Object=MibTableColumn
eocDeviceIpAddress=_EocDeviceIpAddress_Object((1,3,6,1,4,1,17409,2,3,11,1,1,10),_EocDeviceIpAddress_Type())
eocDeviceIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:eocDeviceIpAddress.setStatus(_A)
_EocDeviceMacAddress_Type=MacAddress
_EocDeviceMacAddress_Object=MibTableColumn
eocDeviceMacAddress=_EocDeviceMacAddress_Object((1,3,6,1,4,1,17409,2,3,11,1,1,11),_EocDeviceMacAddress_Type())
eocDeviceMacAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:eocDeviceMacAddress.setStatus(_A)
class _EocDeviceMibVersion_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_EocDeviceMibVersion_Type.__name__=_C
_EocDeviceMibVersion_Object=MibTableColumn
eocDeviceMibVersion=_EocDeviceMibVersion_Object((1,3,6,1,4,1,17409,2,3,11,1,1,12),_EocDeviceMibVersion_Type())
eocDeviceMibVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eocDeviceMibVersion.setStatus(_A)
class _EocDeviceSnmpVersion_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('v1',1),('v2c',2),('v3',3)))
_EocDeviceSnmpVersion_Type.__name__=_G
_EocDeviceSnmpVersion_Object=MibTableColumn
eocDeviceSnmpVersion=_EocDeviceSnmpVersion_Object((1,3,6,1,4,1,17409,2,3,11,1,1,13),_EocDeviceSnmpVersion_Type())
eocDeviceSnmpVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:eocDeviceSnmpVersion.setStatus(_A)
_EocDeviceMngVlan_Type=Integer32
_EocDeviceMngVlan_Object=MibTableColumn
eocDeviceMngVlan=_EocDeviceMngVlan_Object((1,3,6,1,4,1,17409,2,3,11,1,1,14),_EocDeviceMngVlan_Type())
eocDeviceMngVlan.setMaxAccess(_D)
if mibBuilder.loadTexts:eocDeviceMngVlan.setStatus(_A)
_EocDeviceGateWay_Type=IpAddress
_EocDeviceGateWay_Object=MibTableColumn
eocDeviceGateWay=_EocDeviceGateWay_Object((1,3,6,1,4,1,17409,2,3,11,1,1,15),_EocDeviceGateWay_Type())
eocDeviceGateWay.setMaxAccess(_D)
if mibBuilder.loadTexts:eocDeviceGateWay.setStatus(_A)
_EocDeviceSubnetMask_Type=IpAddress
_EocDeviceSubnetMask_Object=MibTableColumn
eocDeviceSubnetMask=_EocDeviceSubnetMask_Object((1,3,6,1,4,1,17409,2,3,11,1,1,16),_EocDeviceSubnetMask_Type())
eocDeviceSubnetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:eocDeviceSubnetMask.setStatus(_A)
_EocDeviceReadCommunity_Type=DisplayString
_EocDeviceReadCommunity_Object=MibTableColumn
eocDeviceReadCommunity=_EocDeviceReadCommunity_Object((1,3,6,1,4,1,17409,2,3,11,1,1,17),_EocDeviceReadCommunity_Type())
eocDeviceReadCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:eocDeviceReadCommunity.setStatus(_A)
_EocDeviceWriteCommunity_Type=DisplayString
_EocDeviceWriteCommunity_Object=MibTableColumn
eocDeviceWriteCommunity=_EocDeviceWriteCommunity_Object((1,3,6,1,4,1,17409,2,3,11,1,1,18),_EocDeviceWriteCommunity_Type())
eocDeviceWriteCommunity.setMaxAccess(_D)
if mibBuilder.loadTexts:eocDeviceWriteCommunity.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'eocDevInfoTable':eocDevInfoTable,'eocDevInfoEntry':eocDevInfoEntry,_H:eDeviceIndex,_I:eCardIndex,_J:ePortIndex,'eocDeviceTechnologyProject':eocDeviceTechnologyProject,'eocDeviceVendorName':eocDeviceVendorName,'eocDeviceProductType':eocDeviceProductType,'eocDeviceSoftwareVersion':eocDeviceSoftwareVersion,'eocDeviceHardwareVersion':eocDeviceHardwareVersion,'eocSeriesNumber':eocSeriesNumber,'eocDeviceIpAddress':eocDeviceIpAddress,'eocDeviceMacAddress':eocDeviceMacAddress,'eocDeviceMibVersion':eocDeviceMibVersion,'eocDeviceSnmpVersion':eocDeviceSnmpVersion,'eocDeviceMngVlan':eocDeviceMngVlan,'eocDeviceGateWay':eocDeviceGateWay,'eocDeviceSubnetMask':eocDeviceSubnetMask,'eocDeviceReadCommunity':eocDeviceReadCommunity,'eocDeviceWriteCommunity':eocDeviceWriteCommunity})