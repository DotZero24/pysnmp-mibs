_I='read-only'
_H='percent'
_G='ifIndex'
_F='IF-MIB'
_E='Integer32'
_D='Unsigned32'
_C='HmEnabledStatus'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HmEnabledStatus,hm2ConfigurationMibs=mibBuilder.importSymbols('HM2-TC-MIB',_C,'hm2ConfigurationMibs')
ifIndex,=mibBuilder.importSymbols(_F,_G)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_D,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hm2TrafficMgmtMib=ModuleIdentity((1,3,6,1,4,1,248,11,31))
if mibBuilder.loadTexts:hm2TrafficMgmtMib.setRevisions(('2011-03-16 00:00',))
_Hm2TrafficMgmtMibNotifications_ObjectIdentity=ObjectIdentity
hm2TrafficMgmtMibNotifications=_Hm2TrafficMgmtMibNotifications_ObjectIdentity((1,3,6,1,4,1,248,11,31,0))
_Hm2TrafficMgmtMibObjects_ObjectIdentity=ObjectIdentity
hm2TrafficMgmtMibObjects=_Hm2TrafficMgmtMibObjects_ObjectIdentity((1,3,6,1,4,1,248,11,31,1))
_Hm2TrafficMgmtIfTable_Object=MibTable
hm2TrafficMgmtIfTable=_Hm2TrafficMgmtIfTable_Object((1,3,6,1,4,1,248,11,31,1,1))
if mibBuilder.loadTexts:hm2TrafficMgmtIfTable.setStatus(_A)
_Hm2TrafficMgmtIfEntry_Object=MibTableRow
hm2TrafficMgmtIfEntry=_Hm2TrafficMgmtIfEntry_Object((1,3,6,1,4,1,248,11,31,1,1,1))
hm2TrafficMgmtIfEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hm2TrafficMgmtIfEntry.setStatus(_A)
class _Hm2TrafficMgmtIfFlowControl_Type(HmEnabledStatus):defaultValue=1
_Hm2TrafficMgmtIfFlowControl_Type.__name__=_C
_Hm2TrafficMgmtIfFlowControl_Object=MibTableColumn
hm2TrafficMgmtIfFlowControl=_Hm2TrafficMgmtIfFlowControl_Object((1,3,6,1,4,1,248,11,31,1,1,1,1),_Hm2TrafficMgmtIfFlowControl_Type())
hm2TrafficMgmtIfFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfFlowControl.setStatus(_A)
class _Hm2TrafficMgmtIfEgressShapingRate_Type(Unsigned32):defaultValue=0
_Hm2TrafficMgmtIfEgressShapingRate_Type.__name__=_D
_Hm2TrafficMgmtIfEgressShapingRate_Object=MibTableColumn
hm2TrafficMgmtIfEgressShapingRate=_Hm2TrafficMgmtIfEgressShapingRate_Object((1,3,6,1,4,1,248,11,31,1,1,1,2),_Hm2TrafficMgmtIfEgressShapingRate_Type())
hm2TrafficMgmtIfEgressShapingRate.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfEgressShapingRate.setStatus(_A)
class _Hm2TrafficMgmtIfEgressShapingRateUnit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('kbps',2)))
_Hm2TrafficMgmtIfEgressShapingRateUnit_Type.__name__=_E
_Hm2TrafficMgmtIfEgressShapingRateUnit_Object=MibTableColumn
hm2TrafficMgmtIfEgressShapingRateUnit=_Hm2TrafficMgmtIfEgressShapingRateUnit_Object((1,3,6,1,4,1,248,11,31,1,1,1,3),_Hm2TrafficMgmtIfEgressShapingRateUnit_Type())
hm2TrafficMgmtIfEgressShapingRateUnit.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2TrafficMgmtIfEgressShapingRateUnit.setStatus(_A)
class _Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),('pps',2)))
_Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Type.__name__=_E
_Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Object=MibTableColumn
hm2TrafficMgmtIfIngressStormCtlThresholdUnit=_Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Object((1,3,6,1,4,1,248,11,31,1,1,1,4),_Hm2TrafficMgmtIfIngressStormCtlThresholdUnit_Type())
hm2TrafficMgmtIfIngressStormCtlThresholdUnit.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfIngressStormCtlThresholdUnit.setStatus(_A)
class _Hm2TrafficMgmtIfIngressStormCtlBcastMode_Type(HmEnabledStatus):defaultValue=2
_Hm2TrafficMgmtIfIngressStormCtlBcastMode_Type.__name__=_C
_Hm2TrafficMgmtIfIngressStormCtlBcastMode_Object=MibTableColumn
hm2TrafficMgmtIfIngressStormCtlBcastMode=_Hm2TrafficMgmtIfIngressStormCtlBcastMode_Object((1,3,6,1,4,1,248,11,31,1,1,1,5),_Hm2TrafficMgmtIfIngressStormCtlBcastMode_Type())
hm2TrafficMgmtIfIngressStormCtlBcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfIngressStormCtlBcastMode.setStatus(_A)
class _Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14880000))
_Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Type.__name__=_D
_Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Object=MibTableColumn
hm2TrafficMgmtIfIngressStormCtlBcastThreshold=_Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Object((1,3,6,1,4,1,248,11,31,1,1,1,6),_Hm2TrafficMgmtIfIngressStormCtlBcastThreshold_Type())
hm2TrafficMgmtIfIngressStormCtlBcastThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfIngressStormCtlBcastThreshold.setStatus(_A)
class _Hm2TrafficMgmtIfIngressStormCtlMcastMode_Type(HmEnabledStatus):defaultValue=2
_Hm2TrafficMgmtIfIngressStormCtlMcastMode_Type.__name__=_C
_Hm2TrafficMgmtIfIngressStormCtlMcastMode_Object=MibTableColumn
hm2TrafficMgmtIfIngressStormCtlMcastMode=_Hm2TrafficMgmtIfIngressStormCtlMcastMode_Object((1,3,6,1,4,1,248,11,31,1,1,1,7),_Hm2TrafficMgmtIfIngressStormCtlMcastMode_Type())
hm2TrafficMgmtIfIngressStormCtlMcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfIngressStormCtlMcastMode.setStatus(_A)
class _Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14880000))
_Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Type.__name__=_D
_Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Object=MibTableColumn
hm2TrafficMgmtIfIngressStormCtlMcastThreshold=_Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Object((1,3,6,1,4,1,248,11,31,1,1,1,8),_Hm2TrafficMgmtIfIngressStormCtlMcastThreshold_Type())
hm2TrafficMgmtIfIngressStormCtlMcastThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfIngressStormCtlMcastThreshold.setStatus(_A)
class _Hm2TrafficMgmtIfIngressStormCtlUcastMode_Type(HmEnabledStatus):defaultValue=2
_Hm2TrafficMgmtIfIngressStormCtlUcastMode_Type.__name__=_C
_Hm2TrafficMgmtIfIngressStormCtlUcastMode_Object=MibTableColumn
hm2TrafficMgmtIfIngressStormCtlUcastMode=_Hm2TrafficMgmtIfIngressStormCtlUcastMode_Object((1,3,6,1,4,1,248,11,31,1,1,1,9),_Hm2TrafficMgmtIfIngressStormCtlUcastMode_Type())
hm2TrafficMgmtIfIngressStormCtlUcastMode.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfIngressStormCtlUcastMode.setStatus(_A)
class _Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,14880000))
_Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Type.__name__=_D
_Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Object=MibTableColumn
hm2TrafficMgmtIfIngressStormCtlUcastThreshold=_Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Object((1,3,6,1,4,1,248,11,31,1,1,1,10),_Hm2TrafficMgmtIfIngressStormCtlUcastThreshold_Type())
hm2TrafficMgmtIfIngressStormCtlUcastThreshold.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtIfIngressStormCtlUcastThreshold.setStatus(_A)
class _Hm2TrafficMgmtFlowControl_Type(HmEnabledStatus):defaultValue=2
_Hm2TrafficMgmtFlowControl_Type.__name__=_C
_Hm2TrafficMgmtFlowControl_Object=MibScalar
hm2TrafficMgmtFlowControl=_Hm2TrafficMgmtFlowControl_Object((1,3,6,1,4,1,248,11,31,1,2),_Hm2TrafficMgmtFlowControl_Type())
hm2TrafficMgmtFlowControl.setMaxAccess(_B)
if mibBuilder.loadTexts:hm2TrafficMgmtFlowControl.setStatus(_A)
class _Hm2TrafficMgmtIngressStormBucketType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('single-bucket',1),('multi-bucket',2)))
_Hm2TrafficMgmtIngressStormBucketType_Type.__name__=_E
_Hm2TrafficMgmtIngressStormBucketType_Object=MibScalar
hm2TrafficMgmtIngressStormBucketType=_Hm2TrafficMgmtIngressStormBucketType_Object((1,3,6,1,4,1,248,11,31,1,3),_Hm2TrafficMgmtIngressStormBucketType_Type())
hm2TrafficMgmtIngressStormBucketType.setMaxAccess(_I)
if mibBuilder.loadTexts:hm2TrafficMgmtIngressStormBucketType.setStatus(_A)
_Hm2TrafficMgmtMibExtensionGroup_ObjectIdentity=ObjectIdentity
hm2TrafficMgmtMibExtensionGroup=_Hm2TrafficMgmtMibExtensionGroup_ObjectIdentity((1,3,6,1,4,1,248,11,31,3))
_Hm2TrafficMgmtNoFlowControl_ObjectIdentity=ObjectIdentity
hm2TrafficMgmtNoFlowControl=_Hm2TrafficMgmtNoFlowControl_ObjectIdentity((1,3,6,1,4,1,248,11,31,3,1))
if mibBuilder.loadTexts:hm2TrafficMgmtNoFlowControl.setStatus(_A)
mibBuilder.exportSymbols('HM2-TRAFFICMGMT-MIB',**{'hm2TrafficMgmtMib':hm2TrafficMgmtMib,'hm2TrafficMgmtMibNotifications':hm2TrafficMgmtMibNotifications,'hm2TrafficMgmtMibObjects':hm2TrafficMgmtMibObjects,'hm2TrafficMgmtIfTable':hm2TrafficMgmtIfTable,'hm2TrafficMgmtIfEntry':hm2TrafficMgmtIfEntry,'hm2TrafficMgmtIfFlowControl':hm2TrafficMgmtIfFlowControl,'hm2TrafficMgmtIfEgressShapingRate':hm2TrafficMgmtIfEgressShapingRate,'hm2TrafficMgmtIfEgressShapingRateUnit':hm2TrafficMgmtIfEgressShapingRateUnit,'hm2TrafficMgmtIfIngressStormCtlThresholdUnit':hm2TrafficMgmtIfIngressStormCtlThresholdUnit,'hm2TrafficMgmtIfIngressStormCtlBcastMode':hm2TrafficMgmtIfIngressStormCtlBcastMode,'hm2TrafficMgmtIfIngressStormCtlBcastThreshold':hm2TrafficMgmtIfIngressStormCtlBcastThreshold,'hm2TrafficMgmtIfIngressStormCtlMcastMode':hm2TrafficMgmtIfIngressStormCtlMcastMode,'hm2TrafficMgmtIfIngressStormCtlMcastThreshold':hm2TrafficMgmtIfIngressStormCtlMcastThreshold,'hm2TrafficMgmtIfIngressStormCtlUcastMode':hm2TrafficMgmtIfIngressStormCtlUcastMode,'hm2TrafficMgmtIfIngressStormCtlUcastThreshold':hm2TrafficMgmtIfIngressStormCtlUcastThreshold,'hm2TrafficMgmtFlowControl':hm2TrafficMgmtFlowControl,'hm2TrafficMgmtIngressStormBucketType':hm2TrafficMgmtIngressStormBucketType,'hm2TrafficMgmtMibExtensionGroup':hm2TrafficMgmtMibExtensionGroup,'hm2TrafficMgmtNoFlowControl':hm2TrafficMgmtNoFlowControl})