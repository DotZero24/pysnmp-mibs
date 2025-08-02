_O='sfpsSwitchPathTablePort'
_N='sfpsSwitchPathTableSwitchMAC'
_M='sfpsServiceCenterPathHashLeaf'
_L='disable'
_K='enable'
_J='sfpsStaticPathPort'
_I='delete'
_H='enabled'
_G='disabled'
_F='other'
_E='CTRON-SFPS-PATH-MIB'
_D='Integer32'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
sfpsChassisRIPPath,sfpsISPSwitchPath,sfpsPathAPI,sfpsPathMaskObj,sfpsStaticPath,sfpsSwitchPath,sfpsSwitchPathAPI,sfpsSwitchPathStats=mibBuilder.importSymbols('CTRON-SFPS-INCLUDE-MIB','sfpsChassisRIPPath','sfpsISPSwitchPath','sfpsPathAPI','sfpsPathMaskObj','sfpsStaticPath','sfpsSwitchPath','sfpsSwitchPathAPI','sfpsSwitchPathStats')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class SfpsAddress(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(6,6));fixedLength=6
class HexInteger(Integer32):0
class _SfpsPathAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*((_F,1),('add',2),(_I,3),('uplink',4),('downlink',5),('diameter',6),('flood-add',7),('flood-delete',8),('force-idle-traffic',9),('remove-traffic-cnx',10)))
_SfpsPathAPIVerb_Type.__name__=_D
_SfpsPathAPIVerb_Object=MibScalar
sfpsPathAPIVerb=_SfpsPathAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,1),_SfpsPathAPIVerb_Type())
sfpsPathAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPIVerb.setStatus(_A)
_SfpsPathAPISwitchMac_Type=SfpsAddress
_SfpsPathAPISwitchMac_Object=MibScalar
sfpsPathAPISwitchMac=_SfpsPathAPISwitchMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,2),_SfpsPathAPISwitchMac_Type())
sfpsPathAPISwitchMac.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPISwitchMac.setStatus(_A)
_SfpsPathAPIPortName_Type=DisplayString
_SfpsPathAPIPortName_Object=MibScalar
sfpsPathAPIPortName=_SfpsPathAPIPortName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,3),_SfpsPathAPIPortName_Type())
sfpsPathAPIPortName.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPIPortName.setStatus(_A)
_SfpsPathAPICost_Type=Integer32
_SfpsPathAPICost_Object=MibScalar
sfpsPathAPICost=_SfpsPathAPICost_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,4),_SfpsPathAPICost_Type())
sfpsPathAPICost.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPICost.setStatus(_A)
_SfpsPathAPIHop_Type=Integer32
_SfpsPathAPIHop_Object=MibScalar
sfpsPathAPIHop=_SfpsPathAPIHop_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,5),_SfpsPathAPIHop_Type())
sfpsPathAPIHop.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPIHop.setStatus(_A)
_SfpsPathAPIID_Type=Integer32
_SfpsPathAPIID_Object=MibScalar
sfpsPathAPIID=_SfpsPathAPIID_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,6),_SfpsPathAPIID_Type())
sfpsPathAPIID.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPIID.setStatus(_A)
_SfpsPathAPIInPort_Type=SfpsAddress
_SfpsPathAPIInPort_Object=MibScalar
sfpsPathAPIInPort=_SfpsPathAPIInPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,7),_SfpsPathAPIInPort_Type())
sfpsPathAPIInPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPIInPort.setStatus(_A)
_SfpsPathAPISrcMac_Type=SfpsAddress
_SfpsPathAPISrcMac_Object=MibScalar
sfpsPathAPISrcMac=_SfpsPathAPISrcMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,8),_SfpsPathAPISrcMac_Type())
sfpsPathAPISrcMac.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPISrcMac.setStatus(_A)
_SfpsPathAPIDstMac_Type=SfpsAddress
_SfpsPathAPIDstMac_Object=MibScalar
sfpsPathAPIDstMac=_SfpsPathAPIDstMac_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,3,9),_SfpsPathAPIDstMac_Type())
sfpsPathAPIDstMac.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathAPIDstMac.setStatus(_A)
_SfpsStaticPathTable_Object=MibTable
sfpsStaticPathTable=_SfpsStaticPathTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,4,1))
if mibBuilder.loadTexts:sfpsStaticPathTable.setStatus(_A)
_SfpsStaticPathEntry_Object=MibTableRow
sfpsStaticPathEntry=_SfpsStaticPathEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,4,1,1))
sfpsStaticPathEntry.setIndexNames((0,_E,_J))
if mibBuilder.loadTexts:sfpsStaticPathEntry.setStatus(_A)
_SfpsStaticPathPort_Type=Integer32
_SfpsStaticPathPort_Object=MibTableColumn
sfpsStaticPathPort=_SfpsStaticPathPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,4,1,1,1),_SfpsStaticPathPort_Type())
sfpsStaticPathPort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsStaticPathPort.setStatus(_A)
class _SfpsStaticPathFloodEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_H,3)))
_SfpsStaticPathFloodEnabled_Type.__name__=_D
_SfpsStaticPathFloodEnabled_Object=MibTableColumn
sfpsStaticPathFloodEnabled=_SfpsStaticPathFloodEnabled_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,4,1,1,2),_SfpsStaticPathFloodEnabled_Type())
sfpsStaticPathFloodEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsStaticPathFloodEnabled.setStatus(_A)
class _SfpsStaticPathUplinkEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_H,3)))
_SfpsStaticPathUplinkEnabled_Type.__name__=_D
_SfpsStaticPathUplinkEnabled_Object=MibTableColumn
sfpsStaticPathUplinkEnabled=_SfpsStaticPathUplinkEnabled_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,4,1,1,3),_SfpsStaticPathUplinkEnabled_Type())
sfpsStaticPathUplinkEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsStaticPathUplinkEnabled.setStatus(_A)
class _SfpsStaticPathDownlinkEnabled_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_H,3)))
_SfpsStaticPathDownlinkEnabled_Type.__name__=_D
_SfpsStaticPathDownlinkEnabled_Object=MibTableColumn
sfpsStaticPathDownlinkEnabled=_SfpsStaticPathDownlinkEnabled_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,4,1,1,4),_SfpsStaticPathDownlinkEnabled_Type())
sfpsStaticPathDownlinkEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsStaticPathDownlinkEnabled.setStatus(_A)
_SfpsPathMaskObjLogPortMask_Type=DisplayString
_SfpsPathMaskObjLogPortMask_Object=MibScalar
sfpsPathMaskObjLogPortMask=_SfpsPathMaskObjLogPortMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,1),_SfpsPathMaskObjLogPortMask_Type())
sfpsPathMaskObjLogPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjLogPortMask.setStatus(_A)
_SfpsPathMaskObjPhysPortMask_Type=DisplayString
_SfpsPathMaskObjPhysPortMask_Object=MibScalar
sfpsPathMaskObjPhysPortMask=_SfpsPathMaskObjPhysPortMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,2),_SfpsPathMaskObjPhysPortMask_Type())
sfpsPathMaskObjPhysPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjPhysPortMask.setStatus(_A)
_SfpsPathMaskObjLogResolveMask_Type=DisplayString
_SfpsPathMaskObjLogResolveMask_Object=MibScalar
sfpsPathMaskObjLogResolveMask=_SfpsPathMaskObjLogResolveMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,3),_SfpsPathMaskObjLogResolveMask_Type())
sfpsPathMaskObjLogResolveMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjLogResolveMask.setStatus(_A)
_SfpsPathMaskObjLogFloodNoINB_Type=DisplayString
_SfpsPathMaskObjLogFloodNoINB_Object=MibScalar
sfpsPathMaskObjLogFloodNoINB=_SfpsPathMaskObjLogFloodNoINB_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,4),_SfpsPathMaskObjLogFloodNoINB_Type())
sfpsPathMaskObjLogFloodNoINB.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjLogFloodNoINB.setStatus(_A)
_SfpsPathMaskObjPhysResolveMask_Type=DisplayString
_SfpsPathMaskObjPhysResolveMask_Object=MibScalar
sfpsPathMaskObjPhysResolveMask=_SfpsPathMaskObjPhysResolveMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,5),_SfpsPathMaskObjPhysResolveMask_Type())
sfpsPathMaskObjPhysResolveMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjPhysResolveMask.setStatus(_A)
_SfpsPathMaskObjPhysFloodNoINB_Type=DisplayString
_SfpsPathMaskObjPhysFloodNoINB_Object=MibScalar
sfpsPathMaskObjPhysFloodNoINB=_SfpsPathMaskObjPhysFloodNoINB_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,6),_SfpsPathMaskObjPhysFloodNoINB_Type())
sfpsPathMaskObjPhysFloodNoINB.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjPhysFloodNoINB.setStatus(_A)
_SfpsPathMaskObjOldLogPortMask_Type=DisplayString
_SfpsPathMaskObjOldLogPortMask_Object=MibScalar
sfpsPathMaskObjOldLogPortMask=_SfpsPathMaskObjOldLogPortMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,7),_SfpsPathMaskObjOldLogPortMask_Type())
sfpsPathMaskObjOldLogPortMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjOldLogPortMask.setStatus(_A)
_SfpsPathMaskObjPathChangeEvent_Type=Integer32
_SfpsPathMaskObjPathChangeEvent_Object=MibScalar
sfpsPathMaskObjPathChangeEvent=_SfpsPathMaskObjPathChangeEvent_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,8),_SfpsPathMaskObjPathChangeEvent_Type())
sfpsPathMaskObjPathChangeEvent.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathMaskObjPathChangeEvent.setStatus(_A)
_SfpsPathMaskObjPathChangeCounter_Type=Integer32
_SfpsPathMaskObjPathChangeCounter_Object=MibScalar
sfpsPathMaskObjPathChangeCounter=_SfpsPathMaskObjPathChangeCounter_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,9),_SfpsPathMaskObjPathChangeCounter_Type())
sfpsPathMaskObjPathChangeCounter.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjPathChangeCounter.setStatus(_A)
_SfpsPathMaskObjLastChangeTime_Type=TimeTicks
_SfpsPathMaskObjLastChangeTime_Object=MibScalar
sfpsPathMaskObjLastChangeTime=_SfpsPathMaskObjLastChangeTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,10),_SfpsPathMaskObjLastChangeTime_Type())
sfpsPathMaskObjLastChangeTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjLastChangeTime.setStatus(_A)
_SfpsPathMaskObjPathCounterReset_Type=Integer32
_SfpsPathMaskObjPathCounterReset_Object=MibScalar
sfpsPathMaskObjPathCounterReset=_SfpsPathMaskObjPathCounterReset_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,11),_SfpsPathMaskObjPathCounterReset_Type())
sfpsPathMaskObjPathCounterReset.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsPathMaskObjPathCounterReset.setStatus(_A)
_SfpsPathMaskObjIsolatedSwitchMask_Type=DisplayString
_SfpsPathMaskObjIsolatedSwitchMask_Object=MibScalar
sfpsPathMaskObjIsolatedSwitchMask=_SfpsPathMaskObjIsolatedSwitchMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,12),_SfpsPathMaskObjIsolatedSwitchMask_Type())
sfpsPathMaskObjIsolatedSwitchMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjIsolatedSwitchMask.setStatus(_A)
_SfpsPathMaskObjPyhsIsolatedSwitchMask_Type=DisplayString
_SfpsPathMaskObjPyhsIsolatedSwitchMask_Object=MibScalar
sfpsPathMaskObjPyhsIsolatedSwitchMask=_SfpsPathMaskObjPyhsIsolatedSwitchMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,13),_SfpsPathMaskObjPyhsIsolatedSwitchMask_Type())
sfpsPathMaskObjPyhsIsolatedSwitchMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjPyhsIsolatedSwitchMask.setStatus(_A)
_SfpsPathMaskObjLogDownlinkMask_Type=DisplayString
_SfpsPathMaskObjLogDownlinkMask_Object=MibScalar
sfpsPathMaskObjLogDownlinkMask=_SfpsPathMaskObjLogDownlinkMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,14),_SfpsPathMaskObjLogDownlinkMask_Type())
sfpsPathMaskObjLogDownlinkMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjLogDownlinkMask.setStatus(_A)
_SfpsPathMaskObjCoreUplinkMask_Type=DisplayString
_SfpsPathMaskObjCoreUplinkMask_Object=MibScalar
sfpsPathMaskObjCoreUplinkMask=_SfpsPathMaskObjCoreUplinkMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,15),_SfpsPathMaskObjCoreUplinkMask_Type())
sfpsPathMaskObjCoreUplinkMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjCoreUplinkMask.setStatus(_A)
class _SfpsPathMaskObjOverrideFloodMask_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_SfpsPathMaskObjOverrideFloodMask_Type.__name__=_D
_SfpsPathMaskObjOverrideFloodMask_Object=MibScalar
sfpsPathMaskObjOverrideFloodMask=_SfpsPathMaskObjOverrideFloodMask_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,5,16),_SfpsPathMaskObjOverrideFloodMask_Type())
sfpsPathMaskObjOverrideFloodMask.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsPathMaskObjOverrideFloodMask.setStatus(_A)
_SfpsChassisRIPPathNumInTable_Type=Integer32
_SfpsChassisRIPPathNumInTable_Object=MibScalar
sfpsChassisRIPPathNumInTable=_SfpsChassisRIPPathNumInTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,12,1),_SfpsChassisRIPPathNumInTable_Type())
sfpsChassisRIPPathNumInTable.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRIPPathNumInTable.setStatus(_A)
_SfpsChassisRIPPathNumRequests_Type=Integer32
_SfpsChassisRIPPathNumRequests_Object=MibScalar
sfpsChassisRIPPathNumRequests=_SfpsChassisRIPPathNumRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,12,2),_SfpsChassisRIPPathNumRequests_Type())
sfpsChassisRIPPathNumRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRIPPathNumRequests.setStatus(_A)
_SfpsChassisRIPPathNumReplyAck_Type=Integer32
_SfpsChassisRIPPathNumReplyAck_Object=MibScalar
sfpsChassisRIPPathNumReplyAck=_SfpsChassisRIPPathNumReplyAck_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,12,3),_SfpsChassisRIPPathNumReplyAck_Type())
sfpsChassisRIPPathNumReplyAck.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRIPPathNumReplyAck.setStatus(_A)
_SfpsChassisRIPPathNumReplyUnk_Type=Integer32
_SfpsChassisRIPPathNumReplyUnk_Object=MibScalar
sfpsChassisRIPPathNumReplyUnk=_SfpsChassisRIPPathNumReplyUnk_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,5,12,4),_SfpsChassisRIPPathNumReplyUnk_Type())
sfpsChassisRIPPathNumReplyUnk.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsChassisRIPPathNumReplyUnk.setStatus(_A)
_SfpsServiceCenterPathTable_Object=MibTable
sfpsServiceCenterPathTable=_SfpsServiceCenterPathTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1))
if mibBuilder.loadTexts:sfpsServiceCenterPathTable.setStatus(_A)
_SfpsServiceCenterPathEntry_Object=MibTableRow
sfpsServiceCenterPathEntry=_SfpsServiceCenterPathEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1))
sfpsServiceCenterPathEntry.setIndexNames((0,_E,_M))
if mibBuilder.loadTexts:sfpsServiceCenterPathEntry.setStatus(_A)
_SfpsServiceCenterPathHashLeaf_Type=HexInteger
_SfpsServiceCenterPathHashLeaf_Object=MibTableColumn
sfpsServiceCenterPathHashLeaf=_SfpsServiceCenterPathHashLeaf_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1,1),_SfpsServiceCenterPathHashLeaf_Type())
sfpsServiceCenterPathHashLeaf.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterPathHashLeaf.setStatus(_A)
_SfpsServiceCenterPathMetric_Type=Integer32
_SfpsServiceCenterPathMetric_Object=MibTableColumn
sfpsServiceCenterPathMetric=_SfpsServiceCenterPathMetric_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1,2),_SfpsServiceCenterPathMetric_Type())
sfpsServiceCenterPathMetric.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterPathMetric.setStatus(_A)
_SfpsServiceCenterPathName_Type=DisplayString
_SfpsServiceCenterPathName_Object=MibTableColumn
sfpsServiceCenterPathName=_SfpsServiceCenterPathName_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1,3),_SfpsServiceCenterPathName_Type())
sfpsServiceCenterPathName.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterPathName.setStatus(_A)
class _SfpsServiceCenterPathOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('kStatusRunning',1),('kStatusHalted',2),('kStatusPending',3),('kStatusFaulted',4),('kStatusNotStarted',5)))
_SfpsServiceCenterPathOperStatus_Type.__name__=_D
_SfpsServiceCenterPathOperStatus_Object=MibTableColumn
sfpsServiceCenterPathOperStatus=_SfpsServiceCenterPathOperStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1,4),_SfpsServiceCenterPathOperStatus_Type())
sfpsServiceCenterPathOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterPathOperStatus.setStatus(_A)
class _SfpsServiceCenterPathAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_F,1),(_L,2),(_K,3)))
_SfpsServiceCenterPathAdminStatus_Type.__name__=_D
_SfpsServiceCenterPathAdminStatus_Object=MibTableColumn
sfpsServiceCenterPathAdminStatus=_SfpsServiceCenterPathAdminStatus_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1,5),_SfpsServiceCenterPathAdminStatus_Type())
sfpsServiceCenterPathAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsServiceCenterPathAdminStatus.setStatus(_A)
_SfpsServiceCenterPathStatusTime_Type=TimeTicks
_SfpsServiceCenterPathStatusTime_Object=MibTableColumn
sfpsServiceCenterPathStatusTime=_SfpsServiceCenterPathStatusTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1,6),_SfpsServiceCenterPathStatusTime_Type())
sfpsServiceCenterPathStatusTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterPathStatusTime.setStatus(_A)
_SfpsServiceCenterPathRequests_Type=Integer32
_SfpsServiceCenterPathRequests_Object=MibTableColumn
sfpsServiceCenterPathRequests=_SfpsServiceCenterPathRequests_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1,7),_SfpsServiceCenterPathRequests_Type())
sfpsServiceCenterPathRequests.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterPathRequests.setStatus(_A)
_SfpsServiceCenterPathResponses_Type=Integer32
_SfpsServiceCenterPathResponses_Object=MibTableColumn
sfpsServiceCenterPathResponses=_SfpsServiceCenterPathResponses_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,1,1,8),_SfpsServiceCenterPathResponses_Type())
sfpsServiceCenterPathResponses.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsServiceCenterPathResponses.setStatus(_A)
_SfpsSwitchPathStatsNumEntries_Type=Integer32
_SfpsSwitchPathStatsNumEntries_Object=MibScalar
sfpsSwitchPathStatsNumEntries=_SfpsSwitchPathStatsNumEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,1),_SfpsSwitchPathStatsNumEntries_Type())
sfpsSwitchPathStatsNumEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsNumEntries.setStatus(_A)
_SfpsSwitchPathStatsMaxEntries_Type=Integer32
_SfpsSwitchPathStatsMaxEntries_Object=MibScalar
sfpsSwitchPathStatsMaxEntries=_SfpsSwitchPathStatsMaxEntries_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,2),_SfpsSwitchPathStatsMaxEntries_Type())
sfpsSwitchPathStatsMaxEntries.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsMaxEntries.setStatus(_A)
_SfpsSwitchPathStatsTableSize_Type=Integer32
_SfpsSwitchPathStatsTableSize_Object=MibScalar
sfpsSwitchPathStatsTableSize=_SfpsSwitchPathStatsTableSize_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,3),_SfpsSwitchPathStatsTableSize_Type())
sfpsSwitchPathStatsTableSize.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsTableSize.setStatus(_A)
_SfpsSwitchPathStatsMemUsage_Type=Integer32
_SfpsSwitchPathStatsMemUsage_Object=MibScalar
sfpsSwitchPathStatsMemUsage=_SfpsSwitchPathStatsMemUsage_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,4),_SfpsSwitchPathStatsMemUsage_Type())
sfpsSwitchPathStatsMemUsage.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsMemUsage.setStatus(_A)
_SfpsSwitchPathStatsActiveLocal_Type=Integer32
_SfpsSwitchPathStatsActiveLocal_Object=MibScalar
sfpsSwitchPathStatsActiveLocal=_SfpsSwitchPathStatsActiveLocal_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,5),_SfpsSwitchPathStatsActiveLocal_Type())
sfpsSwitchPathStatsActiveLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsActiveLocal.setStatus(_A)
_SfpsSwitchPathStatsActiveRemote_Type=Integer32
_SfpsSwitchPathStatsActiveRemote_Object=MibScalar
sfpsSwitchPathStatsActiveRemote=_SfpsSwitchPathStatsActiveRemote_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,6),_SfpsSwitchPathStatsActiveRemote_Type())
sfpsSwitchPathStatsActiveRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsActiveRemote.setStatus(_A)
_SfpsSwitchPathStatsStaticRemote_Type=Integer32
_SfpsSwitchPathStatsStaticRemote_Object=MibScalar
sfpsSwitchPathStatsStaticRemote=_SfpsSwitchPathStatsStaticRemote_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,7),_SfpsSwitchPathStatsStaticRemote_Type())
sfpsSwitchPathStatsStaticRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsStaticRemote.setStatus(_A)
_SfpsSwitchPathStatsDeadLocal_Type=Integer32
_SfpsSwitchPathStatsDeadLocal_Object=MibScalar
sfpsSwitchPathStatsDeadLocal=_SfpsSwitchPathStatsDeadLocal_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,8),_SfpsSwitchPathStatsDeadLocal_Type())
sfpsSwitchPathStatsDeadLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsDeadLocal.setStatus(_A)
_SfpsSwitchPathStatsDeadRemote_Type=Integer32
_SfpsSwitchPathStatsDeadRemote_Object=MibScalar
sfpsSwitchPathStatsDeadRemote=_SfpsSwitchPathStatsDeadRemote_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,9),_SfpsSwitchPathStatsDeadRemote_Type())
sfpsSwitchPathStatsDeadRemote.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsDeadRemote.setStatus(_A)
_SfpsSwitchPathStatsReapReady_Type=Integer32
_SfpsSwitchPathStatsReapReady_Object=MibScalar
sfpsSwitchPathStatsReapReady=_SfpsSwitchPathStatsReapReady_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,10),_SfpsSwitchPathStatsReapReady_Type())
sfpsSwitchPathStatsReapReady.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsReapReady.setStatus(_A)
_SfpsSwitchPathStatsReapAt_Type=Integer32
_SfpsSwitchPathStatsReapAt_Object=MibScalar
sfpsSwitchPathStatsReapAt=_SfpsSwitchPathStatsReapAt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,11),_SfpsSwitchPathStatsReapAt_Type())
sfpsSwitchPathStatsReapAt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsReapAt.setStatus(_A)
_SfpsSwitchPathStatsReapCount_Type=Integer32
_SfpsSwitchPathStatsReapCount_Object=MibScalar
sfpsSwitchPathStatsReapCount=_SfpsSwitchPathStatsReapCount_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,12),_SfpsSwitchPathStatsReapCount_Type())
sfpsSwitchPathStatsReapCount.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsReapCount.setStatus(_A)
_SfpsSwitchPathStatsPathReq_Type=Integer32
_SfpsSwitchPathStatsPathReq_Object=MibScalar
sfpsSwitchPathStatsPathReq=_SfpsSwitchPathStatsPathReq_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,13),_SfpsSwitchPathStatsPathReq_Type())
sfpsSwitchPathStatsPathReq.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsPathReq.setStatus(_A)
_SfpsSwitchPathStatsPathAck_Type=Integer32
_SfpsSwitchPathStatsPathAck_Object=MibScalar
sfpsSwitchPathStatsPathAck=_SfpsSwitchPathStatsPathAck_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,14),_SfpsSwitchPathStatsPathAck_Type())
sfpsSwitchPathStatsPathAck.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsPathAck.setStatus(_A)
_SfpsSwitchPathStatsPathNak_Type=Integer32
_SfpsSwitchPathStatsPathNak_Object=MibScalar
sfpsSwitchPathStatsPathNak=_SfpsSwitchPathStatsPathNak_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,15),_SfpsSwitchPathStatsPathNak_Type())
sfpsSwitchPathStatsPathNak.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsPathNak.setStatus(_A)
_SfpsSwitchPathStatsPathUnk_Type=Integer32
_SfpsSwitchPathStatsPathUnk_Object=MibScalar
sfpsSwitchPathStatsPathUnk=_SfpsSwitchPathStatsPathUnk_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,16),_SfpsSwitchPathStatsPathUnk_Type())
sfpsSwitchPathStatsPathUnk.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsPathUnk.setStatus(_A)
_SfpsSwitchPathStatsLocateReq_Type=Integer32
_SfpsSwitchPathStatsLocateReq_Object=MibScalar
sfpsSwitchPathStatsLocateReq=_SfpsSwitchPathStatsLocateReq_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,17),_SfpsSwitchPathStatsLocateReq_Type())
sfpsSwitchPathStatsLocateReq.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsLocateReq.setStatus(_A)
_SfpsSwitchPathStatsLocateAck_Type=Integer32
_SfpsSwitchPathStatsLocateAck_Object=MibScalar
sfpsSwitchPathStatsLocateAck=_SfpsSwitchPathStatsLocateAck_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,18),_SfpsSwitchPathStatsLocateAck_Type())
sfpsSwitchPathStatsLocateAck.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsLocateAck.setStatus(_A)
_SfpsSwitchPathStatsLocateNak_Type=Integer32
_SfpsSwitchPathStatsLocateNak_Object=MibScalar
sfpsSwitchPathStatsLocateNak=_SfpsSwitchPathStatsLocateNak_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,19),_SfpsSwitchPathStatsLocateNak_Type())
sfpsSwitchPathStatsLocateNak.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsLocateNak.setStatus(_A)
_SfpsSwitchPathStatsLocateUnk_Type=Integer32
_SfpsSwitchPathStatsLocateUnk_Object=MibScalar
sfpsSwitchPathStatsLocateUnk=_SfpsSwitchPathStatsLocateUnk_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,20),_SfpsSwitchPathStatsLocateUnk_Type())
sfpsSwitchPathStatsLocateUnk.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsLocateUnk.setStatus(_A)
_SfpsSwitchPathStatsSndDblBack_Type=Integer32
_SfpsSwitchPathStatsSndDblBack_Object=MibScalar
sfpsSwitchPathStatsSndDblBack=_SfpsSwitchPathStatsSndDblBack_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,21),_SfpsSwitchPathStatsSndDblBack_Type())
sfpsSwitchPathStatsSndDblBack.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsSndDblBack.setStatus(_A)
_SfpsSwitchPathStatsRcdDblBack_Type=Integer32
_SfpsSwitchPathStatsRcdDblBack_Object=MibScalar
sfpsSwitchPathStatsRcdDblBack=_SfpsSwitchPathStatsRcdDblBack_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,1,22),_SfpsSwitchPathStatsRcdDblBack_Type())
sfpsSwitchPathStatsRcdDblBack.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathStatsRcdDblBack.setStatus(_A)
class _SfpsSwitchPathAPIVerb_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8)));namedValues=NamedValues(*((_F,1),('addFind',2),('lose',3),(_I,4),('clearTable',5),('resetStats',6),('setReapAt',7),('setMaxRcvDblBck',8)))
_SfpsSwitchPathAPIVerb_Type.__name__=_D
_SfpsSwitchPathAPIVerb_Object=MibScalar
sfpsSwitchPathAPIVerb=_SfpsSwitchPathAPIVerb_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,2,1),_SfpsSwitchPathAPIVerb_Type())
sfpsSwitchPathAPIVerb.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSwitchPathAPIVerb.setStatus(_A)
_SfpsSwitchPathAPIPort_Type=Integer32
_SfpsSwitchPathAPIPort_Object=MibScalar
sfpsSwitchPathAPIPort=_SfpsSwitchPathAPIPort_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,2,2),_SfpsSwitchPathAPIPort_Type())
sfpsSwitchPathAPIPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSwitchPathAPIPort.setStatus(_A)
_SfpsSwitchPathAPIBaseMAC_Type=SfpsAddress
_SfpsSwitchPathAPIBaseMAC_Object=MibScalar
sfpsSwitchPathAPIBaseMAC=_SfpsSwitchPathAPIBaseMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,2,3),_SfpsSwitchPathAPIBaseMAC_Type())
sfpsSwitchPathAPIBaseMAC.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSwitchPathAPIBaseMAC.setStatus(_A)
_SfpsSwitchPathAPIReapAt_Type=Integer32
_SfpsSwitchPathAPIReapAt_Object=MibScalar
sfpsSwitchPathAPIReapAt=_SfpsSwitchPathAPIReapAt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,2,4),_SfpsSwitchPathAPIReapAt_Type())
sfpsSwitchPathAPIReapAt.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSwitchPathAPIReapAt.setStatus(_A)
_SfpsSwitchPathAPIMaxRcvDblBack_Type=Integer32
_SfpsSwitchPathAPIMaxRcvDblBack_Object=MibScalar
sfpsSwitchPathAPIMaxRcvDblBack=_SfpsSwitchPathAPIMaxRcvDblBack_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,2,5),_SfpsSwitchPathAPIMaxRcvDblBack_Type())
sfpsSwitchPathAPIMaxRcvDblBack.setMaxAccess(_C)
if mibBuilder.loadTexts:sfpsSwitchPathAPIMaxRcvDblBack.setStatus(_A)
_SfpsSwitchPathTable_Object=MibTable
sfpsSwitchPathTable=_SfpsSwitchPathTable_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3))
if mibBuilder.loadTexts:sfpsSwitchPathTable.setStatus(_A)
_SfpsSwitchPathTableEntry_Object=MibTableRow
sfpsSwitchPathTableEntry=_SfpsSwitchPathTableEntry_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1))
sfpsSwitchPathTableEntry.setIndexNames((0,_E,_N),(0,_E,_O))
if mibBuilder.loadTexts:sfpsSwitchPathTableEntry.setStatus(_A)
_SfpsSwitchPathTableSwitchMAC_Type=SfpsAddress
_SfpsSwitchPathTableSwitchMAC_Object=MibTableColumn
sfpsSwitchPathTableSwitchMAC=_SfpsSwitchPathTableSwitchMAC_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,1),_SfpsSwitchPathTableSwitchMAC_Type())
sfpsSwitchPathTableSwitchMAC.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableSwitchMAC.setStatus(_A)
_SfpsSwitchPathTablePort_Type=Integer32
_SfpsSwitchPathTablePort_Object=MibTableColumn
sfpsSwitchPathTablePort=_SfpsSwitchPathTablePort_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,2),_SfpsSwitchPathTablePort_Type())
sfpsSwitchPathTablePort.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTablePort.setStatus(_A)
_SfpsSwitchPathTableIsActive_Type=Integer32
_SfpsSwitchPathTableIsActive_Object=MibTableColumn
sfpsSwitchPathTableIsActive=_SfpsSwitchPathTableIsActive_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,3),_SfpsSwitchPathTableIsActive_Type())
sfpsSwitchPathTableIsActive.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableIsActive.setStatus(_A)
_SfpsSwitchPathTableIsStatic_Type=Integer32
_SfpsSwitchPathTableIsStatic_Object=MibTableColumn
sfpsSwitchPathTableIsStatic=_SfpsSwitchPathTableIsStatic_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,4),_SfpsSwitchPathTableIsStatic_Type())
sfpsSwitchPathTableIsStatic.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableIsStatic.setStatus(_A)
_SfpsSwitchPathTableIsLocal_Type=Integer32
_SfpsSwitchPathTableIsLocal_Object=MibTableColumn
sfpsSwitchPathTableIsLocal=_SfpsSwitchPathTableIsLocal_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,5),_SfpsSwitchPathTableIsLocal_Type())
sfpsSwitchPathTableIsLocal.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableIsLocal.setStatus(_A)
_SfpsSwitchPathTableRefCnt_Type=Integer32
_SfpsSwitchPathTableRefCnt_Object=MibTableColumn
sfpsSwitchPathTableRefCnt=_SfpsSwitchPathTableRefCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,6),_SfpsSwitchPathTableRefCnt_Type())
sfpsSwitchPathTableRefCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableRefCnt.setStatus(_A)
_SfpsSwitchPathTableRefTime_Type=TimeTicks
_SfpsSwitchPathTableRefTime_Object=MibTableColumn
sfpsSwitchPathTableRefTime=_SfpsSwitchPathTableRefTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,7),_SfpsSwitchPathTableRefTime_Type())
sfpsSwitchPathTableRefTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableRefTime.setStatus(_A)
_SfpsSwitchPathTableFoundCnt_Type=Integer32
_SfpsSwitchPathTableFoundCnt_Object=MibTableColumn
sfpsSwitchPathTableFoundCnt=_SfpsSwitchPathTableFoundCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,8),_SfpsSwitchPathTableFoundCnt_Type())
sfpsSwitchPathTableFoundCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableFoundCnt.setStatus(_A)
_SfpsSwitchPathTableFoundTime_Type=TimeTicks
_SfpsSwitchPathTableFoundTime_Object=MibTableColumn
sfpsSwitchPathTableFoundTime=_SfpsSwitchPathTableFoundTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,9),_SfpsSwitchPathTableFoundTime_Type())
sfpsSwitchPathTableFoundTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableFoundTime.setStatus(_A)
_SfpsSwitchPathTableLostCnt_Type=Integer32
_SfpsSwitchPathTableLostCnt_Object=MibTableColumn
sfpsSwitchPathTableLostCnt=_SfpsSwitchPathTableLostCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,10),_SfpsSwitchPathTableLostCnt_Type())
sfpsSwitchPathTableLostCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableLostCnt.setStatus(_A)
_SfpsSwitchPathTableLostTime_Type=TimeTicks
_SfpsSwitchPathTableLostTime_Object=MibTableColumn
sfpsSwitchPathTableLostTime=_SfpsSwitchPathTableLostTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,11),_SfpsSwitchPathTableLostTime_Type())
sfpsSwitchPathTableLostTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableLostTime.setStatus(_A)
_SfpsSwitchPathTableSrcDblBackCnt_Type=Integer32
_SfpsSwitchPathTableSrcDblBackCnt_Object=MibTableColumn
sfpsSwitchPathTableSrcDblBackCnt=_SfpsSwitchPathTableSrcDblBackCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,12),_SfpsSwitchPathTableSrcDblBackCnt_Type())
sfpsSwitchPathTableSrcDblBackCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableSrcDblBackCnt.setStatus(_A)
_SfpsSwitchPathTableSrcDblBackTime_Type=TimeTicks
_SfpsSwitchPathTableSrcDblBackTime_Object=MibTableColumn
sfpsSwitchPathTableSrcDblBackTime=_SfpsSwitchPathTableSrcDblBackTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,13),_SfpsSwitchPathTableSrcDblBackTime_Type())
sfpsSwitchPathTableSrcDblBackTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableSrcDblBackTime.setStatus(_A)
_SfpsSwitchPathTableRcvDblBackCnt_Type=Integer32
_SfpsSwitchPathTableRcvDblBackCnt_Object=MibTableColumn
sfpsSwitchPathTableRcvDblBackCnt=_SfpsSwitchPathTableRcvDblBackCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,14),_SfpsSwitchPathTableRcvDblBackCnt_Type())
sfpsSwitchPathTableRcvDblBackCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableRcvDblBackCnt.setStatus(_A)
_SfpsSwitchPathTableRcvDblBackTime_Type=TimeTicks
_SfpsSwitchPathTableRcvDblBackTime_Object=MibTableColumn
sfpsSwitchPathTableRcvDblBackTime=_SfpsSwitchPathTableRcvDblBackTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,15),_SfpsSwitchPathTableRcvDblBackTime_Type())
sfpsSwitchPathTableRcvDblBackTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableRcvDblBackTime.setStatus(_A)
_SfpsSwitchPathTableDirReapCnt_Type=Integer32
_SfpsSwitchPathTableDirReapCnt_Object=MibTableColumn
sfpsSwitchPathTableDirReapCnt=_SfpsSwitchPathTableDirReapCnt_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,16),_SfpsSwitchPathTableDirReapCnt_Type())
sfpsSwitchPathTableDirReapCnt.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableDirReapCnt.setStatus(_A)
_SfpsSwitchPathTableDirReapTime_Type=TimeTicks
_SfpsSwitchPathTableDirReapTime_Object=MibTableColumn
sfpsSwitchPathTableDirReapTime=_SfpsSwitchPathTableDirReapTime_Object((1,3,6,1,4,1,52,4,2,4,2,2,2,4,7,2,3,1,17),_SfpsSwitchPathTableDirReapTime_Type())
sfpsSwitchPathTableDirReapTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sfpsSwitchPathTableDirReapTime.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'SfpsAddress':SfpsAddress,'HexInteger':HexInteger,'sfpsPathAPIVerb':sfpsPathAPIVerb,'sfpsPathAPISwitchMac':sfpsPathAPISwitchMac,'sfpsPathAPIPortName':sfpsPathAPIPortName,'sfpsPathAPICost':sfpsPathAPICost,'sfpsPathAPIHop':sfpsPathAPIHop,'sfpsPathAPIID':sfpsPathAPIID,'sfpsPathAPIInPort':sfpsPathAPIInPort,'sfpsPathAPISrcMac':sfpsPathAPISrcMac,'sfpsPathAPIDstMac':sfpsPathAPIDstMac,'sfpsStaticPathTable':sfpsStaticPathTable,'sfpsStaticPathEntry':sfpsStaticPathEntry,_J:sfpsStaticPathPort,'sfpsStaticPathFloodEnabled':sfpsStaticPathFloodEnabled,'sfpsStaticPathUplinkEnabled':sfpsStaticPathUplinkEnabled,'sfpsStaticPathDownlinkEnabled':sfpsStaticPathDownlinkEnabled,'sfpsPathMaskObjLogPortMask':sfpsPathMaskObjLogPortMask,'sfpsPathMaskObjPhysPortMask':sfpsPathMaskObjPhysPortMask,'sfpsPathMaskObjLogResolveMask':sfpsPathMaskObjLogResolveMask,'sfpsPathMaskObjLogFloodNoINB':sfpsPathMaskObjLogFloodNoINB,'sfpsPathMaskObjPhysResolveMask':sfpsPathMaskObjPhysResolveMask,'sfpsPathMaskObjPhysFloodNoINB':sfpsPathMaskObjPhysFloodNoINB,'sfpsPathMaskObjOldLogPortMask':sfpsPathMaskObjOldLogPortMask,'sfpsPathMaskObjPathChangeEvent':sfpsPathMaskObjPathChangeEvent,'sfpsPathMaskObjPathChangeCounter':sfpsPathMaskObjPathChangeCounter,'sfpsPathMaskObjLastChangeTime':sfpsPathMaskObjLastChangeTime,'sfpsPathMaskObjPathCounterReset':sfpsPathMaskObjPathCounterReset,'sfpsPathMaskObjIsolatedSwitchMask':sfpsPathMaskObjIsolatedSwitchMask,'sfpsPathMaskObjPyhsIsolatedSwitchMask':sfpsPathMaskObjPyhsIsolatedSwitchMask,'sfpsPathMaskObjLogDownlinkMask':sfpsPathMaskObjLogDownlinkMask,'sfpsPathMaskObjCoreUplinkMask':sfpsPathMaskObjCoreUplinkMask,'sfpsPathMaskObjOverrideFloodMask':sfpsPathMaskObjOverrideFloodMask,'sfpsChassisRIPPathNumInTable':sfpsChassisRIPPathNumInTable,'sfpsChassisRIPPathNumRequests':sfpsChassisRIPPathNumRequests,'sfpsChassisRIPPathNumReplyAck':sfpsChassisRIPPathNumReplyAck,'sfpsChassisRIPPathNumReplyUnk':sfpsChassisRIPPathNumReplyUnk,'sfpsServiceCenterPathTable':sfpsServiceCenterPathTable,'sfpsServiceCenterPathEntry':sfpsServiceCenterPathEntry,_M:sfpsServiceCenterPathHashLeaf,'sfpsServiceCenterPathMetric':sfpsServiceCenterPathMetric,'sfpsServiceCenterPathName':sfpsServiceCenterPathName,'sfpsServiceCenterPathOperStatus':sfpsServiceCenterPathOperStatus,'sfpsServiceCenterPathAdminStatus':sfpsServiceCenterPathAdminStatus,'sfpsServiceCenterPathStatusTime':sfpsServiceCenterPathStatusTime,'sfpsServiceCenterPathRequests':sfpsServiceCenterPathRequests,'sfpsServiceCenterPathResponses':sfpsServiceCenterPathResponses,'sfpsSwitchPathStatsNumEntries':sfpsSwitchPathStatsNumEntries,'sfpsSwitchPathStatsMaxEntries':sfpsSwitchPathStatsMaxEntries,'sfpsSwitchPathStatsTableSize':sfpsSwitchPathStatsTableSize,'sfpsSwitchPathStatsMemUsage':sfpsSwitchPathStatsMemUsage,'sfpsSwitchPathStatsActiveLocal':sfpsSwitchPathStatsActiveLocal,'sfpsSwitchPathStatsActiveRemote':sfpsSwitchPathStatsActiveRemote,'sfpsSwitchPathStatsStaticRemote':sfpsSwitchPathStatsStaticRemote,'sfpsSwitchPathStatsDeadLocal':sfpsSwitchPathStatsDeadLocal,'sfpsSwitchPathStatsDeadRemote':sfpsSwitchPathStatsDeadRemote,'sfpsSwitchPathStatsReapReady':sfpsSwitchPathStatsReapReady,'sfpsSwitchPathStatsReapAt':sfpsSwitchPathStatsReapAt,'sfpsSwitchPathStatsReapCount':sfpsSwitchPathStatsReapCount,'sfpsSwitchPathStatsPathReq':sfpsSwitchPathStatsPathReq,'sfpsSwitchPathStatsPathAck':sfpsSwitchPathStatsPathAck,'sfpsSwitchPathStatsPathNak':sfpsSwitchPathStatsPathNak,'sfpsSwitchPathStatsPathUnk':sfpsSwitchPathStatsPathUnk,'sfpsSwitchPathStatsLocateReq':sfpsSwitchPathStatsLocateReq,'sfpsSwitchPathStatsLocateAck':sfpsSwitchPathStatsLocateAck,'sfpsSwitchPathStatsLocateNak':sfpsSwitchPathStatsLocateNak,'sfpsSwitchPathStatsLocateUnk':sfpsSwitchPathStatsLocateUnk,'sfpsSwitchPathStatsSndDblBack':sfpsSwitchPathStatsSndDblBack,'sfpsSwitchPathStatsRcdDblBack':sfpsSwitchPathStatsRcdDblBack,'sfpsSwitchPathAPIVerb':sfpsSwitchPathAPIVerb,'sfpsSwitchPathAPIPort':sfpsSwitchPathAPIPort,'sfpsSwitchPathAPIBaseMAC':sfpsSwitchPathAPIBaseMAC,'sfpsSwitchPathAPIReapAt':sfpsSwitchPathAPIReapAt,'sfpsSwitchPathAPIMaxRcvDblBack':sfpsSwitchPathAPIMaxRcvDblBack,'sfpsSwitchPathTable':sfpsSwitchPathTable,'sfpsSwitchPathTableEntry':sfpsSwitchPathTableEntry,_N:sfpsSwitchPathTableSwitchMAC,_O:sfpsSwitchPathTablePort,'sfpsSwitchPathTableIsActive':sfpsSwitchPathTableIsActive,'sfpsSwitchPathTableIsStatic':sfpsSwitchPathTableIsStatic,'sfpsSwitchPathTableIsLocal':sfpsSwitchPathTableIsLocal,'sfpsSwitchPathTableRefCnt':sfpsSwitchPathTableRefCnt,'sfpsSwitchPathTableRefTime':sfpsSwitchPathTableRefTime,'sfpsSwitchPathTableFoundCnt':sfpsSwitchPathTableFoundCnt,'sfpsSwitchPathTableFoundTime':sfpsSwitchPathTableFoundTime,'sfpsSwitchPathTableLostCnt':sfpsSwitchPathTableLostCnt,'sfpsSwitchPathTableLostTime':sfpsSwitchPathTableLostTime,'sfpsSwitchPathTableSrcDblBackCnt':sfpsSwitchPathTableSrcDblBackCnt,'sfpsSwitchPathTableSrcDblBackTime':sfpsSwitchPathTableSrcDblBackTime,'sfpsSwitchPathTableRcvDblBackCnt':sfpsSwitchPathTableRcvDblBackCnt,'sfpsSwitchPathTableRcvDblBackTime':sfpsSwitchPathTableRcvDblBackTime,'sfpsSwitchPathTableDirReapCnt':sfpsSwitchPathTableDirReapCnt,'sfpsSwitchPathTableDirReapTime':sfpsSwitchPathTableDirReapTime})