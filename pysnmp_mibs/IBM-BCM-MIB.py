_L='bcmStaticTargetsIndex'
_K='IBM-BCM-MIB'
_J='Counter32'
_I='other'
_H='down'
_G='up'
_F='Integer32'
_E='busConfIndex'
_D='LAN-EMULATION-BUS-MIB'
_C='read-write'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
busConfEntry,busConfIndex=mibBuilder.importSymbols(_D,'busConfEntry',_E)
AtmLaneAddress,=mibBuilder.importSymbols('LAN-EMULATION-CLIENT-MIB','AtmLaneAddress')
mssServerLanE,=mibBuilder.importSymbols('NWAYSMSS-MIB','mssServerLanE')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_J,'Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
Counter32,Integer32=mibBuilder.importSymbols('SNMPv2-SMI-v1',_J,_F)
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
MacAddress,RowStatus,TruthValue=mibBuilder.importSymbols('SNMPv2-TC-v1','MacAddress','RowStatus','TruthValue')
class BcmCacheAge(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_IbmBcmMIB_ObjectIdentity=ObjectIdentity
ibmBcmMIB=_IbmBcmMIB_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3))
_BcmConfGroup_ObjectIdentity=ObjectIdentity
bcmConfGroup=_BcmConfGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,1))
_BcmConfTable_Object=MibTable
bcmConfTable=_BcmConfTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,1))
if mibBuilder.loadTexts:bcmConfTable.setStatus(_A)
_BcmConfEntry_Object=MibTableRow
bcmConfEntry=_BcmConfEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,1,1))
bcmConfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bcmConfEntry.setStatus(_A)
_BcmRouteCacheEnabled_Type=TruthValue
_BcmRouteCacheEnabled_Object=MibTableColumn
bcmRouteCacheEnabled=_BcmRouteCacheEnabled_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,1,1,1),_BcmRouteCacheEnabled_Type())
bcmRouteCacheEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmRouteCacheEnabled.setStatus(_A)
_BcmStaticTargetsNextId_Type=Integer32
_BcmStaticTargetsNextId_Object=MibScalar
bcmStaticTargetsNextId=_BcmStaticTargetsNextId_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,2),_BcmStaticTargetsNextId_Type())
bcmStaticTargetsNextId.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmStaticTargetsNextId.setStatus(_A)
_BcmStaticTargetsTable_Object=MibTable
bcmStaticTargetsTable=_BcmStaticTargetsTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,3))
if mibBuilder.loadTexts:bcmStaticTargetsTable.setStatus(_A)
_BcmStaticTargetsEntry_Object=MibTableRow
bcmStaticTargetsEntry=_BcmStaticTargetsEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,3,1))
bcmStaticTargetsEntry.setIndexNames((0,_K,_L),(0,_D,_E))
if mibBuilder.loadTexts:bcmStaticTargetsEntry.setStatus(_A)
_BcmStaticTargetsIndex_Type=Integer32
_BcmStaticTargetsIndex_Object=MibTableColumn
bcmStaticTargetsIndex=_BcmStaticTargetsIndex_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,3,1,1),_BcmStaticTargetsIndex_Type())
bcmStaticTargetsIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmStaticTargetsIndex.setStatus(_A)
_BcmStaticTargetsAtmAddress_Type=AtmLaneAddress
_BcmStaticTargetsAtmAddress_Object=MibTableColumn
bcmStaticTargetsAtmAddress=_BcmStaticTargetsAtmAddress_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,3,1,2),_BcmStaticTargetsAtmAddress_Type())
bcmStaticTargetsAtmAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmStaticTargetsAtmAddress.setStatus(_A)
_BcmStaticTargetsMacAddress_Type=MacAddress
_BcmStaticTargetsMacAddress_Object=MibTableColumn
bcmStaticTargetsMacAddress=_BcmStaticTargetsMacAddress_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,3,1,3),_BcmStaticTargetsMacAddress_Type())
bcmStaticTargetsMacAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmStaticTargetsMacAddress.setStatus(_A)
class _BcmStaticTargetsProtocol_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,4)));namedValues=NamedValues(*(('noStaticProtocolDefined',0),('ipx',4)))
_BcmStaticTargetsProtocol_Type.__name__=_F
_BcmStaticTargetsProtocol_Object=MibTableColumn
bcmStaticTargetsProtocol=_BcmStaticTargetsProtocol_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,3,1,4),_BcmStaticTargetsProtocol_Type())
bcmStaticTargetsProtocol.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmStaticTargetsProtocol.setStatus(_A)
_BcmStaticTargetsRowStatus_Type=RowStatus
_BcmStaticTargetsRowStatus_Object=MibTableColumn
bcmStaticTargetsRowStatus=_BcmStaticTargetsRowStatus_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,3,1,5),_BcmStaticTargetsRowStatus_Type())
bcmStaticTargetsRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmStaticTargetsRowStatus.setStatus(_A)
_BcmIpConfTable_Object=MibTable
bcmIpConfTable=_BcmIpConfTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,4))
if mibBuilder.loadTexts:bcmIpConfTable.setStatus(_A)
_BcmIpConfEntry_Object=MibTableRow
bcmIpConfEntry=_BcmIpConfEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,4,1))
bcmIpConfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bcmIpConfEntry.setStatus(_A)
class _BcmIpConfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_BcmIpConfOperStatus_Type.__name__=_F
_BcmIpConfOperStatus_Object=MibTableColumn
bcmIpConfOperStatus=_BcmIpConfOperStatus_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,4,1,1),_BcmIpConfOperStatus_Type())
bcmIpConfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpConfOperStatus.setStatus(_A)
class _BcmIpConfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_H,3)))
_BcmIpConfAdminStatus_Type.__name__=_F
_BcmIpConfAdminStatus_Object=MibTableColumn
bcmIpConfAdminStatus=_BcmIpConfAdminStatus_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,4,1,2),_BcmIpConfAdminStatus_Type())
bcmIpConfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmIpConfAdminStatus.setStatus(_A)
_BcmIpConfCacheAge_Type=BcmCacheAge
_BcmIpConfCacheAge_Object=MibTableColumn
bcmIpConfCacheAge=_BcmIpConfCacheAge_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,4,1,3),_BcmIpConfCacheAge_Type())
bcmIpConfCacheAge.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmIpConfCacheAge.setStatus(_A)
_BcmIpxConfTable_Object=MibTable
bcmIpxConfTable=_BcmIpxConfTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,5))
if mibBuilder.loadTexts:bcmIpxConfTable.setStatus(_A)
_BcmIpxConfEntry_Object=MibTableRow
bcmIpxConfEntry=_BcmIpxConfEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,5,1))
bcmIpxConfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bcmIpxConfEntry.setStatus(_A)
class _BcmIpxConfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_BcmIpxConfOperStatus_Type.__name__=_F
_BcmIpxConfOperStatus_Object=MibTableColumn
bcmIpxConfOperStatus=_BcmIpxConfOperStatus_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,5,1,1),_BcmIpxConfOperStatus_Type())
bcmIpxConfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxConfOperStatus.setStatus(_A)
class _BcmIpxConfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_H,3)))
_BcmIpxConfAdminStatus_Type.__name__=_F
_BcmIpxConfAdminStatus_Object=MibTableColumn
bcmIpxConfAdminStatus=_BcmIpxConfAdminStatus_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,5,1,2),_BcmIpxConfAdminStatus_Type())
bcmIpxConfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmIpxConfAdminStatus.setStatus(_A)
_BcmIpxConfCacheAge_Type=BcmCacheAge
_BcmIpxConfCacheAge_Object=MibTableColumn
bcmIpxConfCacheAge=_BcmIpxConfCacheAge_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,5,1,3),_BcmIpxConfCacheAge_Type())
bcmIpxConfCacheAge.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmIpxConfCacheAge.setStatus(_A)
_BcmNbConfTable_Object=MibTable
bcmNbConfTable=_BcmNbConfTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,6))
if mibBuilder.loadTexts:bcmNbConfTable.setStatus(_A)
_BcmNbConfEntry_Object=MibTableRow
bcmNbConfEntry=_BcmNbConfEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,6,1))
bcmNbConfEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bcmNbConfEntry.setStatus(_A)
class _BcmNbConfOperStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_I,1),(_G,2),(_H,3)))
_BcmNbConfOperStatus_Type.__name__=_F
_BcmNbConfOperStatus_Object=MibTableColumn
bcmNbConfOperStatus=_BcmNbConfOperStatus_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,6,1,1),_BcmNbConfOperStatus_Type())
bcmNbConfOperStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbConfOperStatus.setStatus(_A)
class _BcmNbConfAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3)));namedValues=NamedValues(*((_G,2),(_H,3)))
_BcmNbConfAdminStatus_Type.__name__=_F
_BcmNbConfAdminStatus_Object=MibTableColumn
bcmNbConfAdminStatus=_BcmNbConfAdminStatus_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,6,1,2),_BcmNbConfAdminStatus_Type())
bcmNbConfAdminStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmNbConfAdminStatus.setStatus(_A)
_BcmNbConfCacheAge_Type=BcmCacheAge
_BcmNbConfCacheAge_Object=MibTableColumn
bcmNbConfCacheAge=_BcmNbConfCacheAge_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,1,6,1,3),_BcmNbConfCacheAge_Type())
bcmNbConfCacheAge.setMaxAccess(_C)
if mibBuilder.loadTexts:bcmNbConfCacheAge.setStatus(_A)
_BcmStatGroup_ObjectIdentity=ObjectIdentity
bcmStatGroup=_BcmStatGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,2))
_BcmStatTable_Object=MibTable
bcmStatTable=_BcmStatTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1))
if mibBuilder.loadTexts:bcmStatTable.setStatus(_A)
_BcmStatEntry_Object=MibTableRow
bcmStatEntry=_BcmStatEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1))
bcmStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bcmStatEntry.setStatus(_A)
_BcmFramesReceived_Type=Counter32
_BcmFramesReceived_Object=MibTableColumn
bcmFramesReceived=_BcmFramesReceived_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,1),_BcmFramesReceived_Type())
bcmFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmFramesReceived.setStatus(_A)
_BcmOctetsReceived_Type=Counter32
_BcmOctetsReceived_Object=MibTableColumn
bcmOctetsReceived=_BcmOctetsReceived_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,2),_BcmOctetsReceived_Type())
bcmOctetsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmOctetsReceived.setStatus(_A)
_BcmFramesReturned_Type=Counter32
_BcmFramesReturned_Object=MibTableColumn
bcmFramesReturned=_BcmFramesReturned_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,3),_BcmFramesReturned_Type())
bcmFramesReturned.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmFramesReturned.setStatus(_A)
_BcmOctetsReturned_Type=Counter32
_BcmOctetsReturned_Object=MibTableColumn
bcmOctetsReturned=_BcmOctetsReturned_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,4),_BcmOctetsReturned_Type())
bcmOctetsReturned.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmOctetsReturned.setStatus(_A)
_BcmFramesDiscarded_Type=Counter32
_BcmFramesDiscarded_Object=MibTableColumn
bcmFramesDiscarded=_BcmFramesDiscarded_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,5),_BcmFramesDiscarded_Type())
bcmFramesDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmFramesDiscarded.setStatus(_A)
_BcmOctetsDiscarded_Type=Counter32
_BcmOctetsDiscarded_Object=MibTableColumn
bcmOctetsDiscarded=_BcmOctetsDiscarded_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,6),_BcmOctetsDiscarded_Type())
bcmOctetsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmOctetsDiscarded.setStatus(_A)
_BcmFramesTransmitted_Type=Counter32
_BcmFramesTransmitted_Object=MibTableColumn
bcmFramesTransmitted=_BcmFramesTransmitted_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,7),_BcmFramesTransmitted_Type())
bcmFramesTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmFramesTransmitted.setStatus(_A)
_BcmOctetsTransmitted_Type=Counter32
_BcmOctetsTransmitted_Object=MibTableColumn
bcmOctetsTransmitted=_BcmOctetsTransmitted_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,8),_BcmOctetsTransmitted_Type())
bcmOctetsTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmOctetsTransmitted.setStatus(_A)
_BcmTransmitErrorFrames_Type=Counter32
_BcmTransmitErrorFrames_Object=MibTableColumn
bcmTransmitErrorFrames=_BcmTransmitErrorFrames_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,9),_BcmTransmitErrorFrames_Type())
bcmTransmitErrorFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmTransmitErrorFrames.setStatus(_A)
_BcmTransmitErrorOctets_Type=Counter32
_BcmTransmitErrorOctets_Object=MibTableColumn
bcmTransmitErrorOctets=_BcmTransmitErrorOctets_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,10),_BcmTransmitErrorOctets_Type())
bcmTransmitErrorOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmTransmitErrorOctets.setStatus(_A)
_BcmBroadcastFramesDirectedNoRif_Type=Counter32
_BcmBroadcastFramesDirectedNoRif_Object=MibTableColumn
bcmBroadcastFramesDirectedNoRif=_BcmBroadcastFramesDirectedNoRif_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,11),_BcmBroadcastFramesDirectedNoRif_Type())
bcmBroadcastFramesDirectedNoRif.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmBroadcastFramesDirectedNoRif.setStatus(_A)
_BcmBroadcastFramesDirectedAre_Type=Counter32
_BcmBroadcastFramesDirectedAre_Object=MibTableColumn
bcmBroadcastFramesDirectedAre=_BcmBroadcastFramesDirectedAre_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,12),_BcmBroadcastFramesDirectedAre_Type())
bcmBroadcastFramesDirectedAre.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmBroadcastFramesDirectedAre.setStatus(_A)
_BcmBroadcastFramesDirectedSte_Type=Counter32
_BcmBroadcastFramesDirectedSte_Object=MibTableColumn
bcmBroadcastFramesDirectedSte=_BcmBroadcastFramesDirectedSte_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,13),_BcmBroadcastFramesDirectedSte_Type())
bcmBroadcastFramesDirectedSte.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmBroadcastFramesDirectedSte.setStatus(_A)
_BcmBroadcastFramesDirectedSrf_Type=Counter32
_BcmBroadcastFramesDirectedSrf_Object=MibTableColumn
bcmBroadcastFramesDirectedSrf=_BcmBroadcastFramesDirectedSrf_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,1,1,14),_BcmBroadcastFramesDirectedSrf_Type())
bcmBroadcastFramesDirectedSrf.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmBroadcastFramesDirectedSrf.setStatus(_A)
_BcmIpStatTable_Object=MibTable
bcmIpStatTable=_BcmIpStatTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2))
if mibBuilder.loadTexts:bcmIpStatTable.setStatus(_A)
_BcmIpStatEntry_Object=MibTableRow
bcmIpStatEntry=_BcmIpStatEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1))
bcmIpStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bcmIpStatEntry.setStatus(_A)
_BcmIpFramesReceived_Type=Counter32
_BcmIpFramesReceived_Object=MibTableColumn
bcmIpFramesReceived=_BcmIpFramesReceived_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,1),_BcmIpFramesReceived_Type())
bcmIpFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpFramesReceived.setStatus(_A)
_BcmIpOctetsReceived_Type=Counter32
_BcmIpOctetsReceived_Object=MibTableColumn
bcmIpOctetsReceived=_BcmIpOctetsReceived_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,2),_BcmIpOctetsReceived_Type())
bcmIpOctetsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpOctetsReceived.setStatus(_A)
_BcmIpFramesReturned_Type=Counter32
_BcmIpFramesReturned_Object=MibTableColumn
bcmIpFramesReturned=_BcmIpFramesReturned_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,3),_BcmIpFramesReturned_Type())
bcmIpFramesReturned.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpFramesReturned.setStatus(_A)
_BcmIpOctetsReturned_Type=Counter32
_BcmIpOctetsReturned_Object=MibTableColumn
bcmIpOctetsReturned=_BcmIpOctetsReturned_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,4),_BcmIpOctetsReturned_Type())
bcmIpOctetsReturned.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpOctetsReturned.setStatus(_A)
_BcmIpFramesDiscarded_Type=Counter32
_BcmIpFramesDiscarded_Object=MibTableColumn
bcmIpFramesDiscarded=_BcmIpFramesDiscarded_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,5),_BcmIpFramesDiscarded_Type())
bcmIpFramesDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpFramesDiscarded.setStatus(_A)
_BcmIpOctetsDiscarded_Type=Counter32
_BcmIpOctetsDiscarded_Object=MibTableColumn
bcmIpOctetsDiscarded=_BcmIpOctetsDiscarded_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,6),_BcmIpOctetsDiscarded_Type())
bcmIpOctetsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpOctetsDiscarded.setStatus(_A)
_BcmIpFramesTransmitted_Type=Counter32
_BcmIpFramesTransmitted_Object=MibTableColumn
bcmIpFramesTransmitted=_BcmIpFramesTransmitted_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,7),_BcmIpFramesTransmitted_Type())
bcmIpFramesTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpFramesTransmitted.setStatus(_A)
_BcmIpOctetsTransmitted_Type=Counter32
_BcmIpOctetsTransmitted_Object=MibTableColumn
bcmIpOctetsTransmitted=_BcmIpOctetsTransmitted_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,8),_BcmIpOctetsTransmitted_Type())
bcmIpOctetsTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpOctetsTransmitted.setStatus(_A)
_BcmIpTransmitErrorFrames_Type=Counter32
_BcmIpTransmitErrorFrames_Object=MibTableColumn
bcmIpTransmitErrorFrames=_BcmIpTransmitErrorFrames_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,9),_BcmIpTransmitErrorFrames_Type())
bcmIpTransmitErrorFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpTransmitErrorFrames.setStatus(_A)
_BcmIpTransmitErrorOctets_Type=Counter32
_BcmIpTransmitErrorOctets_Object=MibTableColumn
bcmIpTransmitErrorOctets=_BcmIpTransmitErrorOctets_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,10),_BcmIpTransmitErrorOctets_Type())
bcmIpTransmitErrorOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpTransmitErrorOctets.setStatus(_A)
_BcmIpBroadcastFramesDirectedNoRif_Type=Counter32
_BcmIpBroadcastFramesDirectedNoRif_Object=MibTableColumn
bcmIpBroadcastFramesDirectedNoRif=_BcmIpBroadcastFramesDirectedNoRif_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,11),_BcmIpBroadcastFramesDirectedNoRif_Type())
bcmIpBroadcastFramesDirectedNoRif.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpBroadcastFramesDirectedNoRif.setStatus(_A)
_BcmIpBroadcastFramesDirectedAre_Type=Counter32
_BcmIpBroadcastFramesDirectedAre_Object=MibTableColumn
bcmIpBroadcastFramesDirectedAre=_BcmIpBroadcastFramesDirectedAre_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,12),_BcmIpBroadcastFramesDirectedAre_Type())
bcmIpBroadcastFramesDirectedAre.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpBroadcastFramesDirectedAre.setStatus(_A)
_BcmIpBroadcastFramesDirectedSte_Type=Counter32
_BcmIpBroadcastFramesDirectedSte_Object=MibTableColumn
bcmIpBroadcastFramesDirectedSte=_BcmIpBroadcastFramesDirectedSte_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,13),_BcmIpBroadcastFramesDirectedSte_Type())
bcmIpBroadcastFramesDirectedSte.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpBroadcastFramesDirectedSte.setStatus(_A)
_BcmIpBroadcastFramesDirectedSrf_Type=Counter32
_BcmIpBroadcastFramesDirectedSrf_Object=MibTableColumn
bcmIpBroadcastFramesDirectedSrf=_BcmIpBroadcastFramesDirectedSrf_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,2,1,14),_BcmIpBroadcastFramesDirectedSrf_Type())
bcmIpBroadcastFramesDirectedSrf.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpBroadcastFramesDirectedSrf.setStatus(_A)
_BcmIpxStatTable_Object=MibTable
bcmIpxStatTable=_BcmIpxStatTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3))
if mibBuilder.loadTexts:bcmIpxStatTable.setStatus(_A)
_BcmIpxStatEntry_Object=MibTableRow
bcmIpxStatEntry=_BcmIpxStatEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1))
bcmIpxStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bcmIpxStatEntry.setStatus(_A)
_BcmIpxFramesReceived_Type=Counter32
_BcmIpxFramesReceived_Object=MibTableColumn
bcmIpxFramesReceived=_BcmIpxFramesReceived_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,1),_BcmIpxFramesReceived_Type())
bcmIpxFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxFramesReceived.setStatus(_A)
_BcmIpxOctetsReceived_Type=Counter32
_BcmIpxOctetsReceived_Object=MibTableColumn
bcmIpxOctetsReceived=_BcmIpxOctetsReceived_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,2),_BcmIpxOctetsReceived_Type())
bcmIpxOctetsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxOctetsReceived.setStatus(_A)
_BcmIpxFramesReturned_Type=Counter32
_BcmIpxFramesReturned_Object=MibTableColumn
bcmIpxFramesReturned=_BcmIpxFramesReturned_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,3),_BcmIpxFramesReturned_Type())
bcmIpxFramesReturned.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxFramesReturned.setStatus(_A)
_BcmIpxOctetsReturned_Type=Counter32
_BcmIpxOctetsReturned_Object=MibTableColumn
bcmIpxOctetsReturned=_BcmIpxOctetsReturned_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,4),_BcmIpxOctetsReturned_Type())
bcmIpxOctetsReturned.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxOctetsReturned.setStatus(_A)
_BcmIpxFramesDiscarded_Type=Counter32
_BcmIpxFramesDiscarded_Object=MibTableColumn
bcmIpxFramesDiscarded=_BcmIpxFramesDiscarded_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,5),_BcmIpxFramesDiscarded_Type())
bcmIpxFramesDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxFramesDiscarded.setStatus(_A)
_BcmIpxOctetsDiscarded_Type=Counter32
_BcmIpxOctetsDiscarded_Object=MibTableColumn
bcmIpxOctetsDiscarded=_BcmIpxOctetsDiscarded_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,6),_BcmIpxOctetsDiscarded_Type())
bcmIpxOctetsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxOctetsDiscarded.setStatus(_A)
_BcmIpxFramesTransmitted_Type=Counter32
_BcmIpxFramesTransmitted_Object=MibTableColumn
bcmIpxFramesTransmitted=_BcmIpxFramesTransmitted_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,7),_BcmIpxFramesTransmitted_Type())
bcmIpxFramesTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxFramesTransmitted.setStatus(_A)
_BcmIpxOctetsTransmitted_Type=Counter32
_BcmIpxOctetsTransmitted_Object=MibTableColumn
bcmIpxOctetsTransmitted=_BcmIpxOctetsTransmitted_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,8),_BcmIpxOctetsTransmitted_Type())
bcmIpxOctetsTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxOctetsTransmitted.setStatus(_A)
_BcmIpxTransmitErrorFrames_Type=Counter32
_BcmIpxTransmitErrorFrames_Object=MibTableColumn
bcmIpxTransmitErrorFrames=_BcmIpxTransmitErrorFrames_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,9),_BcmIpxTransmitErrorFrames_Type())
bcmIpxTransmitErrorFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxTransmitErrorFrames.setStatus(_A)
_BcmIpxTransmitErrorOctets_Type=Counter32
_BcmIpxTransmitErrorOctets_Object=MibTableColumn
bcmIpxTransmitErrorOctets=_BcmIpxTransmitErrorOctets_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,10),_BcmIpxTransmitErrorOctets_Type())
bcmIpxTransmitErrorOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxTransmitErrorOctets.setStatus(_A)
_BcmIpxBroadcastFramesDirectedNoRif_Type=Counter32
_BcmIpxBroadcastFramesDirectedNoRif_Object=MibTableColumn
bcmIpxBroadcastFramesDirectedNoRif=_BcmIpxBroadcastFramesDirectedNoRif_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,11),_BcmIpxBroadcastFramesDirectedNoRif_Type())
bcmIpxBroadcastFramesDirectedNoRif.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxBroadcastFramesDirectedNoRif.setStatus(_A)
_BcmIpxBroadcastFramesDirectedAre_Type=Counter32
_BcmIpxBroadcastFramesDirectedAre_Object=MibTableColumn
bcmIpxBroadcastFramesDirectedAre=_BcmIpxBroadcastFramesDirectedAre_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,12),_BcmIpxBroadcastFramesDirectedAre_Type())
bcmIpxBroadcastFramesDirectedAre.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxBroadcastFramesDirectedAre.setStatus(_A)
_BcmIpxBroadcastFramesDirectedSte_Type=Counter32
_BcmIpxBroadcastFramesDirectedSte_Object=MibTableColumn
bcmIpxBroadcastFramesDirectedSte=_BcmIpxBroadcastFramesDirectedSte_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,13),_BcmIpxBroadcastFramesDirectedSte_Type())
bcmIpxBroadcastFramesDirectedSte.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxBroadcastFramesDirectedSte.setStatus(_A)
_BcmIpxBroadcastFramesDirectedSrf_Type=Counter32
_BcmIpxBroadcastFramesDirectedSrf_Object=MibTableColumn
bcmIpxBroadcastFramesDirectedSrf=_BcmIpxBroadcastFramesDirectedSrf_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,3,1,14),_BcmIpxBroadcastFramesDirectedSrf_Type())
bcmIpxBroadcastFramesDirectedSrf.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmIpxBroadcastFramesDirectedSrf.setStatus(_A)
_BcmNbStatTable_Object=MibTable
bcmNbStatTable=_BcmNbStatTable_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4))
if mibBuilder.loadTexts:bcmNbStatTable.setStatus(_A)
_BcmNbStatEntry_Object=MibTableRow
bcmNbStatEntry=_BcmNbStatEntry_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1))
bcmNbStatEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:bcmNbStatEntry.setStatus(_A)
_BcmNbFramesReceived_Type=Counter32
_BcmNbFramesReceived_Object=MibTableColumn
bcmNbFramesReceived=_BcmNbFramesReceived_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,1),_BcmNbFramesReceived_Type())
bcmNbFramesReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbFramesReceived.setStatus(_A)
_BcmNbOctetsReceived_Type=Counter32
_BcmNbOctetsReceived_Object=MibTableColumn
bcmNbOctetsReceived=_BcmNbOctetsReceived_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,2),_BcmNbOctetsReceived_Type())
bcmNbOctetsReceived.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbOctetsReceived.setStatus(_A)
_BcmNbFramesReturned_Type=Counter32
_BcmNbFramesReturned_Object=MibTableColumn
bcmNbFramesReturned=_BcmNbFramesReturned_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,3),_BcmNbFramesReturned_Type())
bcmNbFramesReturned.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbFramesReturned.setStatus(_A)
_BcmNbOctetsReturned_Type=Counter32
_BcmNbOctetsReturned_Object=MibTableColumn
bcmNbOctetsReturned=_BcmNbOctetsReturned_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,4),_BcmNbOctetsReturned_Type())
bcmNbOctetsReturned.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbOctetsReturned.setStatus(_A)
_BcmNbFramesDiscarded_Type=Counter32
_BcmNbFramesDiscarded_Object=MibTableColumn
bcmNbFramesDiscarded=_BcmNbFramesDiscarded_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,5),_BcmNbFramesDiscarded_Type())
bcmNbFramesDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbFramesDiscarded.setStatus(_A)
_BcmNbOctetsDiscarded_Type=Counter32
_BcmNbOctetsDiscarded_Object=MibTableColumn
bcmNbOctetsDiscarded=_BcmNbOctetsDiscarded_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,6),_BcmNbOctetsDiscarded_Type())
bcmNbOctetsDiscarded.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbOctetsDiscarded.setStatus(_A)
_BcmNbFramesTransmitted_Type=Counter32
_BcmNbFramesTransmitted_Object=MibTableColumn
bcmNbFramesTransmitted=_BcmNbFramesTransmitted_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,7),_BcmNbFramesTransmitted_Type())
bcmNbFramesTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbFramesTransmitted.setStatus(_A)
_BcmNbOctetsTransmitted_Type=Counter32
_BcmNbOctetsTransmitted_Object=MibTableColumn
bcmNbOctetsTransmitted=_BcmNbOctetsTransmitted_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,8),_BcmNbOctetsTransmitted_Type())
bcmNbOctetsTransmitted.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbOctetsTransmitted.setStatus(_A)
_BcmNbTransmitErrorFrames_Type=Counter32
_BcmNbTransmitErrorFrames_Object=MibTableColumn
bcmNbTransmitErrorFrames=_BcmNbTransmitErrorFrames_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,9),_BcmNbTransmitErrorFrames_Type())
bcmNbTransmitErrorFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbTransmitErrorFrames.setStatus(_A)
_BcmNbTransmitErrorOctets_Type=Counter32
_BcmNbTransmitErrorOctets_Object=MibTableColumn
bcmNbTransmitErrorOctets=_BcmNbTransmitErrorOctets_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,10),_BcmNbTransmitErrorOctets_Type())
bcmNbTransmitErrorOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbTransmitErrorOctets.setStatus(_A)
_BcmNbBroadcastFramesDirectedNoRif_Type=Counter32
_BcmNbBroadcastFramesDirectedNoRif_Object=MibTableColumn
bcmNbBroadcastFramesDirectedNoRif=_BcmNbBroadcastFramesDirectedNoRif_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,11),_BcmNbBroadcastFramesDirectedNoRif_Type())
bcmNbBroadcastFramesDirectedNoRif.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbBroadcastFramesDirectedNoRif.setStatus(_A)
_BcmNbBroadcastFramesDirectedAre_Type=Counter32
_BcmNbBroadcastFramesDirectedAre_Object=MibTableColumn
bcmNbBroadcastFramesDirectedAre=_BcmNbBroadcastFramesDirectedAre_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,12),_BcmNbBroadcastFramesDirectedAre_Type())
bcmNbBroadcastFramesDirectedAre.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbBroadcastFramesDirectedAre.setStatus(_A)
_BcmNbBroadcastFramesDirectedSte_Type=Counter32
_BcmNbBroadcastFramesDirectedSte_Object=MibTableColumn
bcmNbBroadcastFramesDirectedSte=_BcmNbBroadcastFramesDirectedSte_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,13),_BcmNbBroadcastFramesDirectedSte_Type())
bcmNbBroadcastFramesDirectedSte.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbBroadcastFramesDirectedSte.setStatus(_A)
_BcmNbBroadcastFramesDirectedSrf_Type=Counter32
_BcmNbBroadcastFramesDirectedSrf_Object=MibTableColumn
bcmNbBroadcastFramesDirectedSrf=_BcmNbBroadcastFramesDirectedSrf_Object((1,3,6,1,4,1,2,6,118,1,2,1,3,2,4,1,14),_BcmNbBroadcastFramesDirectedSrf_Type())
bcmNbBroadcastFramesDirectedSrf.setMaxAccess(_B)
if mibBuilder.loadTexts:bcmNbBroadcastFramesDirectedSrf.setStatus(_A)
_BcmMIBConformance_ObjectIdentity=ObjectIdentity
bcmMIBConformance=_BcmMIBConformance_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3))
_BcmMIBGroups_ObjectIdentity=ObjectIdentity
bcmMIBGroups=_BcmMIBGroups_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1))
_BcmCConfGroup_ObjectIdentity=ObjectIdentity
bcmCConfGroup=_BcmCConfGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,1))
_BcmCStaticTargetsConfigGroup_ObjectIdentity=ObjectIdentity
bcmCStaticTargetsConfigGroup=_BcmCStaticTargetsConfigGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,2))
_BcmCIpConfigGroup_ObjectIdentity=ObjectIdentity
bcmCIpConfigGroup=_BcmCIpConfigGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,3))
_BcmCIpxConfigGroup_ObjectIdentity=ObjectIdentity
bcmCIpxConfigGroup=_BcmCIpxConfigGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,4))
_BcmCNbConfigGroup_ObjectIdentity=ObjectIdentity
bcmCNbConfigGroup=_BcmCNbConfigGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,5))
_BcmCStatGroup_ObjectIdentity=ObjectIdentity
bcmCStatGroup=_BcmCStatGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,6))
_BcmCIpStatGroup_ObjectIdentity=ObjectIdentity
bcmCIpStatGroup=_BcmCIpStatGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,7))
_BcmCIpxStatGroup_ObjectIdentity=ObjectIdentity
bcmCIpxStatGroup=_BcmCIpxStatGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,8))
_BcmCNbStatGroup_ObjectIdentity=ObjectIdentity
bcmCNbStatGroup=_BcmCNbStatGroup_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,1,9))
_BcmMIBCompliances_ObjectIdentity=ObjectIdentity
bcmMIBCompliances=_BcmMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,2))
_BcmMIBCompliance_ObjectIdentity=ObjectIdentity
bcmMIBCompliance=_BcmMIBCompliance_ObjectIdentity((1,3,6,1,4,1,2,6,118,1,2,1,3,3,2,1))
mibBuilder.exportSymbols(_K,**{'BcmCacheAge':BcmCacheAge,'ibmBcmMIB':ibmBcmMIB,'bcmConfGroup':bcmConfGroup,'bcmConfTable':bcmConfTable,'bcmConfEntry':bcmConfEntry,'bcmRouteCacheEnabled':bcmRouteCacheEnabled,'bcmStaticTargetsNextId':bcmStaticTargetsNextId,'bcmStaticTargetsTable':bcmStaticTargetsTable,'bcmStaticTargetsEntry':bcmStaticTargetsEntry,_L:bcmStaticTargetsIndex,'bcmStaticTargetsAtmAddress':bcmStaticTargetsAtmAddress,'bcmStaticTargetsMacAddress':bcmStaticTargetsMacAddress,'bcmStaticTargetsProtocol':bcmStaticTargetsProtocol,'bcmStaticTargetsRowStatus':bcmStaticTargetsRowStatus,'bcmIpConfTable':bcmIpConfTable,'bcmIpConfEntry':bcmIpConfEntry,'bcmIpConfOperStatus':bcmIpConfOperStatus,'bcmIpConfAdminStatus':bcmIpConfAdminStatus,'bcmIpConfCacheAge':bcmIpConfCacheAge,'bcmIpxConfTable':bcmIpxConfTable,'bcmIpxConfEntry':bcmIpxConfEntry,'bcmIpxConfOperStatus':bcmIpxConfOperStatus,'bcmIpxConfAdminStatus':bcmIpxConfAdminStatus,'bcmIpxConfCacheAge':bcmIpxConfCacheAge,'bcmNbConfTable':bcmNbConfTable,'bcmNbConfEntry':bcmNbConfEntry,'bcmNbConfOperStatus':bcmNbConfOperStatus,'bcmNbConfAdminStatus':bcmNbConfAdminStatus,'bcmNbConfCacheAge':bcmNbConfCacheAge,'bcmStatGroup':bcmStatGroup,'bcmStatTable':bcmStatTable,'bcmStatEntry':bcmStatEntry,'bcmFramesReceived':bcmFramesReceived,'bcmOctetsReceived':bcmOctetsReceived,'bcmFramesReturned':bcmFramesReturned,'bcmOctetsReturned':bcmOctetsReturned,'bcmFramesDiscarded':bcmFramesDiscarded,'bcmOctetsDiscarded':bcmOctetsDiscarded,'bcmFramesTransmitted':bcmFramesTransmitted,'bcmOctetsTransmitted':bcmOctetsTransmitted,'bcmTransmitErrorFrames':bcmTransmitErrorFrames,'bcmTransmitErrorOctets':bcmTransmitErrorOctets,'bcmBroadcastFramesDirectedNoRif':bcmBroadcastFramesDirectedNoRif,'bcmBroadcastFramesDirectedAre':bcmBroadcastFramesDirectedAre,'bcmBroadcastFramesDirectedSte':bcmBroadcastFramesDirectedSte,'bcmBroadcastFramesDirectedSrf':bcmBroadcastFramesDirectedSrf,'bcmIpStatTable':bcmIpStatTable,'bcmIpStatEntry':bcmIpStatEntry,'bcmIpFramesReceived':bcmIpFramesReceived,'bcmIpOctetsReceived':bcmIpOctetsReceived,'bcmIpFramesReturned':bcmIpFramesReturned,'bcmIpOctetsReturned':bcmIpOctetsReturned,'bcmIpFramesDiscarded':bcmIpFramesDiscarded,'bcmIpOctetsDiscarded':bcmIpOctetsDiscarded,'bcmIpFramesTransmitted':bcmIpFramesTransmitted,'bcmIpOctetsTransmitted':bcmIpOctetsTransmitted,'bcmIpTransmitErrorFrames':bcmIpTransmitErrorFrames,'bcmIpTransmitErrorOctets':bcmIpTransmitErrorOctets,'bcmIpBroadcastFramesDirectedNoRif':bcmIpBroadcastFramesDirectedNoRif,'bcmIpBroadcastFramesDirectedAre':bcmIpBroadcastFramesDirectedAre,'bcmIpBroadcastFramesDirectedSte':bcmIpBroadcastFramesDirectedSte,'bcmIpBroadcastFramesDirectedSrf':bcmIpBroadcastFramesDirectedSrf,'bcmIpxStatTable':bcmIpxStatTable,'bcmIpxStatEntry':bcmIpxStatEntry,'bcmIpxFramesReceived':bcmIpxFramesReceived,'bcmIpxOctetsReceived':bcmIpxOctetsReceived,'bcmIpxFramesReturned':bcmIpxFramesReturned,'bcmIpxOctetsReturned':bcmIpxOctetsReturned,'bcmIpxFramesDiscarded':bcmIpxFramesDiscarded,'bcmIpxOctetsDiscarded':bcmIpxOctetsDiscarded,'bcmIpxFramesTransmitted':bcmIpxFramesTransmitted,'bcmIpxOctetsTransmitted':bcmIpxOctetsTransmitted,'bcmIpxTransmitErrorFrames':bcmIpxTransmitErrorFrames,'bcmIpxTransmitErrorOctets':bcmIpxTransmitErrorOctets,'bcmIpxBroadcastFramesDirectedNoRif':bcmIpxBroadcastFramesDirectedNoRif,'bcmIpxBroadcastFramesDirectedAre':bcmIpxBroadcastFramesDirectedAre,'bcmIpxBroadcastFramesDirectedSte':bcmIpxBroadcastFramesDirectedSte,'bcmIpxBroadcastFramesDirectedSrf':bcmIpxBroadcastFramesDirectedSrf,'bcmNbStatTable':bcmNbStatTable,'bcmNbStatEntry':bcmNbStatEntry,'bcmNbFramesReceived':bcmNbFramesReceived,'bcmNbOctetsReceived':bcmNbOctetsReceived,'bcmNbFramesReturned':bcmNbFramesReturned,'bcmNbOctetsReturned':bcmNbOctetsReturned,'bcmNbFramesDiscarded':bcmNbFramesDiscarded,'bcmNbOctetsDiscarded':bcmNbOctetsDiscarded,'bcmNbFramesTransmitted':bcmNbFramesTransmitted,'bcmNbOctetsTransmitted':bcmNbOctetsTransmitted,'bcmNbTransmitErrorFrames':bcmNbTransmitErrorFrames,'bcmNbTransmitErrorOctets':bcmNbTransmitErrorOctets,'bcmNbBroadcastFramesDirectedNoRif':bcmNbBroadcastFramesDirectedNoRif,'bcmNbBroadcastFramesDirectedAre':bcmNbBroadcastFramesDirectedAre,'bcmNbBroadcastFramesDirectedSte':bcmNbBroadcastFramesDirectedSte,'bcmNbBroadcastFramesDirectedSrf':bcmNbBroadcastFramesDirectedSrf,'bcmMIBConformance':bcmMIBConformance,'bcmMIBGroups':bcmMIBGroups,'bcmCConfGroup':bcmCConfGroup,'bcmCStaticTargetsConfigGroup':bcmCStaticTargetsConfigGroup,'bcmCIpConfigGroup':bcmCIpConfigGroup,'bcmCIpxConfigGroup':bcmCIpxConfigGroup,'bcmCNbConfigGroup':bcmCNbConfigGroup,'bcmCStatGroup':bcmCStatGroup,'bcmCIpStatGroup':bcmCIpStatGroup,'bcmCIpxStatGroup':bcmCIpxStatGroup,'bcmCNbStatGroup':bcmCNbStatGroup,'bcmMIBCompliances':bcmMIBCompliances,'bcmMIBCompliance':bcmMIBCompliance})