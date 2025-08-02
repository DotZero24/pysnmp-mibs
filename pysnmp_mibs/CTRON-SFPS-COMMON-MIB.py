_L='HexInteger'
_K='sfpsDiagLogConfigInstance'
_J='sfpsAOPropertiesTag'
_I='sfpsGenericVersionHash'
_H='CTRON-SFPS-COMMON-MIB'
_G='notSet'
_F='true'
_E='false'
_D='read-only'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsAOProperties,sfpsAOPropertiesAPI,sfpsDiagEventLog,sfpsSystemGenerics=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsAOProperties','sfpsAOPropertiesAPI','sfpsDiagEventLog','sfpsSystemGenerics')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class HexInteger(Integer32):0
_SfpsGenericVersionTable_Object=MibTable
sfpsGenericVersionTable=_SfpsGenericVersionTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,3,1))
if mibBuilder.loadTexts:sfpsGenericVersionTable.setStatus(_A)
_SfpsGenericVersionEntry_Object=MibTableRow
sfpsGenericVersionEntry=_SfpsGenericVersionEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,3,1,1))
sfpsGenericVersionEntry.setIndexNames((0,_H,_I))
if mibBuilder.loadTexts:sfpsGenericVersionEntry.setStatus(_A)
_SfpsGenericVersionHash_Type=Integer32
_SfpsGenericVersionHash_Object=MibTableColumn
sfpsGenericVersionHash=_SfpsGenericVersionHash_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,3,1,1,1),_SfpsGenericVersionHash_Type())
sfpsGenericVersionHash.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsGenericVersionHash.setStatus(_A)
_SfpsGenericVersionName_Type=DisplayString
_SfpsGenericVersionName_Object=MibTableColumn
sfpsGenericVersionName=_SfpsGenericVersionName_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,3,1,1,2),_SfpsGenericVersionName_Type())
sfpsGenericVersionName.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsGenericVersionName.setStatus(_A)
_SfpsGenericVersionVersion_Type=DisplayString
_SfpsGenericVersionVersion_Object=MibTableColumn
sfpsGenericVersionVersion=_SfpsGenericVersionVersion_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,3,1,1,3),_SfpsGenericVersionVersion_Type())
sfpsGenericVersionVersion.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsGenericVersionVersion.setStatus(_A)
_SfpsGenericVersionMIBRev_Type=DisplayString
_SfpsGenericVersionMIBRev_Object=MibTableColumn
sfpsGenericVersionMIBRev=_SfpsGenericVersionMIBRev_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,3,1,1,4),_SfpsGenericVersionMIBRev_Type())
sfpsGenericVersionMIBRev.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsGenericVersionMIBRev.setStatus(_A)
_SfpsAOPropertiesTable_Object=MibTable
sfpsAOPropertiesTable=_SfpsAOPropertiesTable_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1))
if mibBuilder.loadTexts:sfpsAOPropertiesTable.setStatus(_A)
_SfpsAOPropertiesEntry_Object=MibTableRow
sfpsAOPropertiesEntry=_SfpsAOPropertiesEntry_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1))
sfpsAOPropertiesEntry.setIndexNames((0,_H,_J))
if mibBuilder.loadTexts:sfpsAOPropertiesEntry.setStatus(_A)
_SfpsAOPropertiesTag_Type=Integer32
_SfpsAOPropertiesTag_Object=MibTableColumn
sfpsAOPropertiesTag=_SfpsAOPropertiesTag_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,1),_SfpsAOPropertiesTag_Type())
sfpsAOPropertiesTag.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesTag.setStatus(_A)
_SfpsAOPropertiesTagDescriptor_Type=OctetString
_SfpsAOPropertiesTagDescriptor_Object=MibTableColumn
sfpsAOPropertiesTagDescriptor=_SfpsAOPropertiesTagDescriptor_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,2),_SfpsAOPropertiesTagDescriptor_Type())
sfpsAOPropertiesTagDescriptor.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesTagDescriptor.setStatus(_A)
_SfpsAOPropertiesPrettyType_Type=OctetString
_SfpsAOPropertiesPrettyType_Object=MibTableColumn
sfpsAOPropertiesPrettyType=_SfpsAOPropertiesPrettyType_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,3),_SfpsAOPropertiesPrettyType_Type())
sfpsAOPropertiesPrettyType.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesPrettyType.setStatus(_A)
_SfpsAOPropertiesNumBytes_Type=Integer32
_SfpsAOPropertiesNumBytes_Object=MibTableColumn
sfpsAOPropertiesNumBytes=_SfpsAOPropertiesNumBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,4),_SfpsAOPropertiesNumBytes_Type())
sfpsAOPropertiesNumBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesNumBytes.setStatus(_A)
class _SfpsAOPropertiesIsLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsAOPropertiesIsLimit_Type.__name__=_C
_SfpsAOPropertiesIsLimit_Object=MibTableColumn
sfpsAOPropertiesIsLimit=_SfpsAOPropertiesIsLimit_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,5),_SfpsAOPropertiesIsLimit_Type())
sfpsAOPropertiesIsLimit.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesIsLimit.setStatus(_A)
class _SfpsAOPropertiesIsMobile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsAOPropertiesIsMobile_Type.__name__=_C
_SfpsAOPropertiesIsMobile_Object=MibTableColumn
sfpsAOPropertiesIsMobile=_SfpsAOPropertiesIsMobile_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,6),_SfpsAOPropertiesIsMobile_Type())
sfpsAOPropertiesIsMobile.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesIsMobile.setStatus(_A)
class _SfpsAOPropertiesIsSingle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsAOPropertiesIsSingle_Type.__name__=_C
_SfpsAOPropertiesIsSingle_Object=MibTableColumn
sfpsAOPropertiesIsSingle=_SfpsAOPropertiesIsSingle_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,7),_SfpsAOPropertiesIsSingle_Type())
sfpsAOPropertiesIsSingle.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesIsSingle.setStatus(_A)
class _SfpsAOPropertiesNoBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsAOPropertiesNoBlock_Type.__name__=_C
_SfpsAOPropertiesNoBlock_Object=MibTableColumn
sfpsAOPropertiesNoBlock=_SfpsAOPropertiesNoBlock_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,8),_SfpsAOPropertiesNoBlock_Type())
sfpsAOPropertiesNoBlock.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesNoBlock.setStatus(_A)
class _SfpsAOPropertiesNoDelta_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_E,1),(_F,2)))
_SfpsAOPropertiesNoDelta_Type.__name__=_C
_SfpsAOPropertiesNoDelta_Object=MibTableColumn
sfpsAOPropertiesNoDelta=_SfpsAOPropertiesNoDelta_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,1,1,9),_SfpsAOPropertiesNoDelta_Type())
sfpsAOPropertiesNoDelta.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesNoDelta.setStatus(_A)
_SfpsAOPropertiesAPITag_Type=Integer32
_SfpsAOPropertiesAPITag_Object=MibScalar
sfpsAOPropertiesAPITag=_SfpsAOPropertiesAPITag_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,1),_SfpsAOPropertiesAPITag_Type())
sfpsAOPropertiesAPITag.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAOPropertiesAPITag.setStatus(_A)
_SfpsAOPropertiesAPITagString_Type=Integer32
_SfpsAOPropertiesAPITagString_Object=MibScalar
sfpsAOPropertiesAPITagString=_SfpsAOPropertiesAPITagString_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,2),_SfpsAOPropertiesAPITagString_Type())
sfpsAOPropertiesAPITagString.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesAPITagString.setStatus(_A)
_SfpsAOPropertiesAPIPrettyType_Type=Integer32
_SfpsAOPropertiesAPIPrettyType_Object=MibScalar
sfpsAOPropertiesAPIPrettyType=_SfpsAOPropertiesAPIPrettyType_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,3),_SfpsAOPropertiesAPIPrettyType_Type())
sfpsAOPropertiesAPIPrettyType.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesAPIPrettyType.setStatus(_A)
_SfpsAOPropertiesAPINumBytes_Type=Integer32
_SfpsAOPropertiesAPINumBytes_Object=MibScalar
sfpsAOPropertiesAPINumBytes=_SfpsAOPropertiesAPINumBytes_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,4),_SfpsAOPropertiesAPINumBytes_Type())
sfpsAOPropertiesAPINumBytes.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsAOPropertiesAPINumBytes.setStatus(_A)
class _SfpsAOPropertiesAPIIsLimit_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsAOPropertiesAPIIsLimit_Type.__name__=_C
_SfpsAOPropertiesAPIIsLimit_Object=MibScalar
sfpsAOPropertiesAPIIsLimit=_SfpsAOPropertiesAPIIsLimit_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,5),_SfpsAOPropertiesAPIIsLimit_Type())
sfpsAOPropertiesAPIIsLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAOPropertiesAPIIsLimit.setStatus(_A)
class _SfpsAOPropertiesAPIIsMobile_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsAOPropertiesAPIIsMobile_Type.__name__=_C
_SfpsAOPropertiesAPIIsMobile_Object=MibScalar
sfpsAOPropertiesAPIIsMobile=_SfpsAOPropertiesAPIIsMobile_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,6),_SfpsAOPropertiesAPIIsMobile_Type())
sfpsAOPropertiesAPIIsMobile.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAOPropertiesAPIIsMobile.setStatus(_A)
class _SfpsAOPropertiesAPIIsSingle_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsAOPropertiesAPIIsSingle_Type.__name__=_C
_SfpsAOPropertiesAPIIsSingle_Object=MibScalar
sfpsAOPropertiesAPIIsSingle=_SfpsAOPropertiesAPIIsSingle_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,7),_SfpsAOPropertiesAPIIsSingle_Type())
sfpsAOPropertiesAPIIsSingle.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAOPropertiesAPIIsSingle.setStatus(_A)
class _SfpsAOPropertiesAPINoBlock_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsAOPropertiesAPINoBlock_Type.__name__=_C
_SfpsAOPropertiesAPINoBlock_Object=MibScalar
sfpsAOPropertiesAPINoBlock=_SfpsAOPropertiesAPINoBlock_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,8),_SfpsAOPropertiesAPINoBlock_Type())
sfpsAOPropertiesAPINoBlock.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAOPropertiesAPINoBlock.setStatus(_A)
class _SfpsAOPropertiesAPINoDelta_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_G,1),(_E,2),(_F,3)))
_SfpsAOPropertiesAPINoDelta_Type.__name__=_C
_SfpsAOPropertiesAPINoDelta_Object=MibScalar
sfpsAOPropertiesAPINoDelta=_SfpsAOPropertiesAPINoDelta_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,9),_SfpsAOPropertiesAPINoDelta_Type())
sfpsAOPropertiesAPINoDelta.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAOPropertiesAPINoDelta.setStatus(_A)
class _SfpsAOPropertiesAPIAction_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('readProperties',1),('setProperties',2)))
_SfpsAOPropertiesAPIAction_Type.__name__=_C
_SfpsAOPropertiesAPIAction_Object=MibScalar
sfpsAOPropertiesAPIAction=_SfpsAOPropertiesAPIAction_Object((1,3,6,1,4,1,52,4,2,4,2,1,1,5,2,10),_SfpsAOPropertiesAPIAction_Type())
sfpsAOPropertiesAPIAction.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsAOPropertiesAPIAction.setStatus(_A)
_SfpsDiagLogConfigTable_Object=MibTable
sfpsDiagLogConfigTable=_SfpsDiagLogConfigTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1))
if mibBuilder.loadTexts:sfpsDiagLogConfigTable.setStatus(_A)
_SfpsDiagLogConfigEntry_Object=MibTableRow
sfpsDiagLogConfigEntry=_SfpsDiagLogConfigEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1))
sfpsDiagLogConfigEntry.setIndexNames((0,_H,_K))
if mibBuilder.loadTexts:sfpsDiagLogConfigEntry.setStatus(_A)
_SfpsDiagLogConfigInstance_Type=Integer32
_SfpsDiagLogConfigInstance_Object=MibTableColumn
sfpsDiagLogConfigInstance=_SfpsDiagLogConfigInstance_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,1),_SfpsDiagLogConfigInstance_Type())
sfpsDiagLogConfigInstance.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDiagLogConfigInstance.setStatus(_A)
class _SfpsDiagLogConfigStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('other',1),('disabled',2),('enabled',3)))
_SfpsDiagLogConfigStatus_Type.__name__=_C
_SfpsDiagLogConfigStatus_Object=MibTableColumn
sfpsDiagLogConfigStatus=_SfpsDiagLogConfigStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,2),_SfpsDiagLogConfigStatus_Type())
sfpsDiagLogConfigStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigStatus.setStatus(_A)
_SfpsDiagLogConfigIndex_Type=Integer32
_SfpsDiagLogConfigIndex_Object=MibTableColumn
sfpsDiagLogConfigIndex=_SfpsDiagLogConfigIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,3),_SfpsDiagLogConfigIndex_Type())
sfpsDiagLogConfigIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:sfpsDiagLogConfigIndex.setStatus(_A)
_SfpsDiagLogConfigStart_Type=Integer32
_SfpsDiagLogConfigStart_Object=MibTableColumn
sfpsDiagLogConfigStart=_SfpsDiagLogConfigStart_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,4),_SfpsDiagLogConfigStart_Type())
sfpsDiagLogConfigStart.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigStart.setStatus(_A)
_SfpsDiagLogConfigStop_Type=Integer32
_SfpsDiagLogConfigStop_Object=MibTableColumn
sfpsDiagLogConfigStop=_SfpsDiagLogConfigStop_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,5),_SfpsDiagLogConfigStop_Type())
sfpsDiagLogConfigStop.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigStop.setStatus(_A)
_SfpsDiagLogConfigLogIndex_Type=Integer32
_SfpsDiagLogConfigLogIndex_Object=MibTableColumn
sfpsDiagLogConfigLogIndex=_SfpsDiagLogConfigLogIndex_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,6),_SfpsDiagLogConfigLogIndex_Type())
sfpsDiagLogConfigLogIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigLogIndex.setStatus(_A)
_SfpsDiagLogConfigFilterMatch_Type=Integer32
_SfpsDiagLogConfigFilterMatch_Object=MibTableColumn
sfpsDiagLogConfigFilterMatch=_SfpsDiagLogConfigFilterMatch_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,7),_SfpsDiagLogConfigFilterMatch_Type())
sfpsDiagLogConfigFilterMatch.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigFilterMatch.setStatus(_A)
_SfpsDiagLogConfigFilterStart_Type=Integer32
_SfpsDiagLogConfigFilterStart_Object=MibTableColumn
sfpsDiagLogConfigFilterStart=_SfpsDiagLogConfigFilterStart_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,8),_SfpsDiagLogConfigFilterStart_Type())
sfpsDiagLogConfigFilterStart.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigFilterStart.setStatus(_A)
_SfpsDiagLogConfigFilterStop_Type=Integer32
_SfpsDiagLogConfigFilterStop_Object=MibTableColumn
sfpsDiagLogConfigFilterStop=_SfpsDiagLogConfigFilterStop_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,9),_SfpsDiagLogConfigFilterStop_Type())
sfpsDiagLogConfigFilterStop.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigFilterStop.setStatus(_A)
class _SfpsDiagLogAccessPortControl_Type(HexInteger):defaultValue=0
_SfpsDiagLogAccessPortControl_Type.__name__=_L
_SfpsDiagLogAccessPortControl_Object=MibTableColumn
sfpsDiagLogAccessPortControl=_SfpsDiagLogAccessPortControl_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,10),_SfpsDiagLogAccessPortControl_Type())
sfpsDiagLogAccessPortControl.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogAccessPortControl.setStatus(_A)
class _SfpsDiagLogCallIdleTime_Type(Integer32):defaultValue=60
_SfpsDiagLogCallIdleTime_Type.__name__=_C
_SfpsDiagLogCallIdleTime_Object=MibTableColumn
sfpsDiagLogCallIdleTime=_SfpsDiagLogCallIdleTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,11),_SfpsDiagLogCallIdleTime_Type())
sfpsDiagLogCallIdleTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogCallIdleTime.setStatus(_A)
class _SfpsDiagLogFilterAddTimer_Type(Integer32):defaultValue=900
_SfpsDiagLogFilterAddTimer_Type.__name__=_C
_SfpsDiagLogFilterAddTimer_Object=MibTableColumn
sfpsDiagLogFilterAddTimer=_SfpsDiagLogFilterAddTimer_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,12),_SfpsDiagLogFilterAddTimer_Type())
sfpsDiagLogFilterAddTimer.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogFilterAddTimer.setStatus(_A)
_SfpsDiagLogRedirectorWakeup_Type=Integer32
_SfpsDiagLogRedirectorWakeup_Object=MibTableColumn
sfpsDiagLogRedirectorWakeup=_SfpsDiagLogRedirectorWakeup_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,13),_SfpsDiagLogRedirectorWakeup_Type())
sfpsDiagLogRedirectorWakeup.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogRedirectorWakeup.setStatus(_A)
class _SfpsDiagLogRedirectorNumPackets_Type(Integer32):defaultValue=64
_SfpsDiagLogRedirectorNumPackets_Type.__name__=_C
_SfpsDiagLogRedirectorNumPackets_Object=MibTableColumn
sfpsDiagLogRedirectorNumPackets=_SfpsDiagLogRedirectorNumPackets_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,14),_SfpsDiagLogRedirectorNumPackets_Type())
sfpsDiagLogRedirectorNumPackets.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogRedirectorNumPackets.setStatus(_A)
class _SfpsDiagLogEndSystemTimeout_Type(Integer32):defaultValue=600
_SfpsDiagLogEndSystemTimeout_Type.__name__=_C
_SfpsDiagLogEndSystemTimeout_Object=MibTableColumn
sfpsDiagLogEndSystemTimeout=_SfpsDiagLogEndSystemTimeout_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,15),_SfpsDiagLogEndSystemTimeout_Type())
sfpsDiagLogEndSystemTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogEndSystemTimeout.setStatus(_A)
class _SfpsDiagLogSwitchIdleInterval_Type(Integer32):defaultValue=30
_SfpsDiagLogSwitchIdleInterval_Type.__name__=_C
_SfpsDiagLogSwitchIdleInterval_Object=MibTableColumn
sfpsDiagLogSwitchIdleInterval=_SfpsDiagLogSwitchIdleInterval_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,16),_SfpsDiagLogSwitchIdleInterval_Type())
sfpsDiagLogSwitchIdleInterval.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogSwitchIdleInterval.setStatus(_A)
_SfpsDiagLogInlnFltrAgeTime_Type=Integer32
_SfpsDiagLogInlnFltrAgeTime_Object=MibTableColumn
sfpsDiagLogInlnFltrAgeTime=_SfpsDiagLogInlnFltrAgeTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,17),_SfpsDiagLogInlnFltrAgeTime_Type())
sfpsDiagLogInlnFltrAgeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogInlnFltrAgeTime.setStatus(_A)
_SfpsDiagLogConfigDebug9_Type=Integer32
_SfpsDiagLogConfigDebug9_Object=MibTableColumn
sfpsDiagLogConfigDebug9=_SfpsDiagLogConfigDebug9_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,18),_SfpsDiagLogConfigDebug9_Type())
sfpsDiagLogConfigDebug9.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigDebug9.setStatus(_A)
_SfpsDiagLogSignalThrottle_Type=Integer32
_SfpsDiagLogSignalThrottle_Object=MibTableColumn
sfpsDiagLogSignalThrottle=_SfpsDiagLogSignalThrottle_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,19),_SfpsDiagLogSignalThrottle_Type())
sfpsDiagLogSignalThrottle.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogSignalThrottle.setStatus(_A)
class _SfpsDiagLogConfigOther_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('string',1),('integer',2)))
_SfpsDiagLogConfigOther_Type.__name__=_C
_SfpsDiagLogConfigOther_Object=MibTableColumn
sfpsDiagLogConfigOther=_SfpsDiagLogConfigOther_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,20),_SfpsDiagLogConfigOther_Type())
sfpsDiagLogConfigOther.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigOther.setStatus(_A)
_SfpsDiagLogConfigSoftReset_Type=Integer32
_SfpsDiagLogConfigSoftReset_Object=MibTableColumn
sfpsDiagLogConfigSoftReset=_SfpsDiagLogConfigSoftReset_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,21),_SfpsDiagLogConfigSoftReset_Type())
sfpsDiagLogConfigSoftReset.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigSoftReset.setStatus(_A)
_SfpsDiagLogConfigSFPSVlan_Type=Integer32
_SfpsDiagLogConfigSFPSVlan_Object=MibTableColumn
sfpsDiagLogConfigSFPSVlan=_SfpsDiagLogConfigSFPSVlan_Object((1,3,6,1,4,1,52,4,2,4,2,2,6,1,1,1,22),_SfpsDiagLogConfigSFPSVlan_Type())
sfpsDiagLogConfigSFPSVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsDiagLogConfigSFPSVlan.setStatus(_A)
mibBuilder.exportSymbols(_H,**{_L:HexInteger,'sfpsGenericVersionTable':sfpsGenericVersionTable,'sfpsGenericVersionEntry':sfpsGenericVersionEntry,_I:sfpsGenericVersionHash,'sfpsGenericVersionName':sfpsGenericVersionName,'sfpsGenericVersionVersion':sfpsGenericVersionVersion,'sfpsGenericVersionMIBRev':sfpsGenericVersionMIBRev,'sfpsAOPropertiesTable':sfpsAOPropertiesTable,'sfpsAOPropertiesEntry':sfpsAOPropertiesEntry,_J:sfpsAOPropertiesTag,'sfpsAOPropertiesTagDescriptor':sfpsAOPropertiesTagDescriptor,'sfpsAOPropertiesPrettyType':sfpsAOPropertiesPrettyType,'sfpsAOPropertiesNumBytes':sfpsAOPropertiesNumBytes,'sfpsAOPropertiesIsLimit':sfpsAOPropertiesIsLimit,'sfpsAOPropertiesIsMobile':sfpsAOPropertiesIsMobile,'sfpsAOPropertiesIsSingle':sfpsAOPropertiesIsSingle,'sfpsAOPropertiesNoBlock':sfpsAOPropertiesNoBlock,'sfpsAOPropertiesNoDelta':sfpsAOPropertiesNoDelta,'sfpsAOPropertiesAPITag':sfpsAOPropertiesAPITag,'sfpsAOPropertiesAPITagString':sfpsAOPropertiesAPITagString,'sfpsAOPropertiesAPIPrettyType':sfpsAOPropertiesAPIPrettyType,'sfpsAOPropertiesAPINumBytes':sfpsAOPropertiesAPINumBytes,'sfpsAOPropertiesAPIIsLimit':sfpsAOPropertiesAPIIsLimit,'sfpsAOPropertiesAPIIsMobile':sfpsAOPropertiesAPIIsMobile,'sfpsAOPropertiesAPIIsSingle':sfpsAOPropertiesAPIIsSingle,'sfpsAOPropertiesAPINoBlock':sfpsAOPropertiesAPINoBlock,'sfpsAOPropertiesAPINoDelta':sfpsAOPropertiesAPINoDelta,'sfpsAOPropertiesAPIAction':sfpsAOPropertiesAPIAction,'sfpsDiagLogConfigTable':sfpsDiagLogConfigTable,'sfpsDiagLogConfigEntry':sfpsDiagLogConfigEntry,_K:sfpsDiagLogConfigInstance,'sfpsDiagLogConfigStatus':sfpsDiagLogConfigStatus,'sfpsDiagLogConfigIndex':sfpsDiagLogConfigIndex,'sfpsDiagLogConfigStart':sfpsDiagLogConfigStart,'sfpsDiagLogConfigStop':sfpsDiagLogConfigStop,'sfpsDiagLogConfigLogIndex':sfpsDiagLogConfigLogIndex,'sfpsDiagLogConfigFilterMatch':sfpsDiagLogConfigFilterMatch,'sfpsDiagLogConfigFilterStart':sfpsDiagLogConfigFilterStart,'sfpsDiagLogConfigFilterStop':sfpsDiagLogConfigFilterStop,'sfpsDiagLogAccessPortControl':sfpsDiagLogAccessPortControl,'sfpsDiagLogCallIdleTime':sfpsDiagLogCallIdleTime,'sfpsDiagLogFilterAddTimer':sfpsDiagLogFilterAddTimer,'sfpsDiagLogRedirectorWakeup':sfpsDiagLogRedirectorWakeup,'sfpsDiagLogRedirectorNumPackets':sfpsDiagLogRedirectorNumPackets,'sfpsDiagLogEndSystemTimeout':sfpsDiagLogEndSystemTimeout,'sfpsDiagLogSwitchIdleInterval':sfpsDiagLogSwitchIdleInterval,'sfpsDiagLogInlnFltrAgeTime':sfpsDiagLogInlnFltrAgeTime,'sfpsDiagLogConfigDebug9':sfpsDiagLogConfigDebug9,'sfpsDiagLogSignalThrottle':sfpsDiagLogSignalThrottle,'sfpsDiagLogConfigOther':sfpsDiagLogConfigOther,'sfpsDiagLogConfigSoftReset':sfpsDiagLogConfigSoftReset,'sfpsDiagLogConfigSFPSVlan':sfpsDiagLogConfigSFPSVlan})