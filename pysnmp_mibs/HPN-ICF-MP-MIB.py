_T='hpnicfMpMandatoryGroup'
_S='hpnicfMpMemberlinkMpStatus'
_R='hpnicfMpMemberlinkDescr'
_Q='hpnicfMpSentSequence'
_P='hpnicfMpRcvdSequence'
_O='hpnicfMpInterleavedPkts'
_N='hpnicfMpUnassignedPkts'
_M='hpnicfMpReorderedPkts'
_L='hpnicfMpLostFragments'
_K='hpnicfMpBundledSlot'
_J='hpnicfMpBundleName'
_I='hpnicfMpMultilinkDescr'
_H='hpnicfMpMemberlinkIfIndex'
_G='hpnicfMpBundledMemberCnt'
_F='hpnicfMpMemberlinkSeqNumber'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='HPN-ICF-MP-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hpnicfRhw,=mibBuilder.importSymbols('HPN-ICF-OID-MIB','hpnicfRhw')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
hpnicfMultilinkPPP=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,8,33))
_HpnicfMpObjects_ObjectIdentity=ObjectIdentity
hpnicfMpObjects=_HpnicfMpObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,33,1))
_HpnicfMpMultilinkTable_Object=MibTable
hpnicfMpMultilinkTable=_HpnicfMpMultilinkTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1))
if mibBuilder.loadTexts:hpnicfMpMultilinkTable.setStatus(_A)
_HpnicfMpMultilinkEntry_Object=MibTableRow
hpnicfMpMultilinkEntry=_HpnicfMpMultilinkEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1))
hpnicfMpMultilinkEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:hpnicfMpMultilinkEntry.setStatus(_A)
_HpnicfMpMultilinkDescr_Type=DisplayString
_HpnicfMpMultilinkDescr_Object=MibTableColumn
hpnicfMpMultilinkDescr=_HpnicfMpMultilinkDescr_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,1),_HpnicfMpMultilinkDescr_Type())
hpnicfMpMultilinkDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpMultilinkDescr.setStatus(_A)
_HpnicfMpBundleName_Type=DisplayString
_HpnicfMpBundleName_Object=MibTableColumn
hpnicfMpBundleName=_HpnicfMpBundleName_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,2),_HpnicfMpBundleName_Type())
hpnicfMpBundleName.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpBundleName.setStatus(_A)
_HpnicfMpBundledSlot_Type=Integer32
_HpnicfMpBundledSlot_Object=MibTableColumn
hpnicfMpBundledSlot=_HpnicfMpBundledSlot_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,3),_HpnicfMpBundledSlot_Type())
hpnicfMpBundledSlot.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpBundledSlot.setStatus(_A)
_HpnicfMpBundledMemberCnt_Type=Integer32
_HpnicfMpBundledMemberCnt_Object=MibTableColumn
hpnicfMpBundledMemberCnt=_HpnicfMpBundledMemberCnt_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,4),_HpnicfMpBundledMemberCnt_Type())
hpnicfMpBundledMemberCnt.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpBundledMemberCnt.setStatus(_A)
_HpnicfMpLostFragments_Type=Counter32
_HpnicfMpLostFragments_Object=MibTableColumn
hpnicfMpLostFragments=_HpnicfMpLostFragments_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,5),_HpnicfMpLostFragments_Type())
hpnicfMpLostFragments.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpLostFragments.setStatus(_A)
_HpnicfMpReorderedPkts_Type=Counter32
_HpnicfMpReorderedPkts_Object=MibTableColumn
hpnicfMpReorderedPkts=_HpnicfMpReorderedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,6),_HpnicfMpReorderedPkts_Type())
hpnicfMpReorderedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpReorderedPkts.setStatus(_A)
_HpnicfMpUnassignedPkts_Type=Counter32
_HpnicfMpUnassignedPkts_Object=MibTableColumn
hpnicfMpUnassignedPkts=_HpnicfMpUnassignedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,7),_HpnicfMpUnassignedPkts_Type())
hpnicfMpUnassignedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpUnassignedPkts.setStatus(_A)
_HpnicfMpInterleavedPkts_Type=Counter32
_HpnicfMpInterleavedPkts_Object=MibTableColumn
hpnicfMpInterleavedPkts=_HpnicfMpInterleavedPkts_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,8),_HpnicfMpInterleavedPkts_Type())
hpnicfMpInterleavedPkts.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpInterleavedPkts.setStatus(_A)
_HpnicfMpRcvdSequence_Type=Integer32
_HpnicfMpRcvdSequence_Object=MibTableColumn
hpnicfMpRcvdSequence=_HpnicfMpRcvdSequence_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,9),_HpnicfMpRcvdSequence_Type())
hpnicfMpRcvdSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpRcvdSequence.setStatus(_A)
_HpnicfMpSentSequence_Type=Integer32
_HpnicfMpSentSequence_Object=MibTableColumn
hpnicfMpSentSequence=_HpnicfMpSentSequence_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,1,1,10),_HpnicfMpSentSequence_Type())
hpnicfMpSentSequence.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpSentSequence.setStatus(_A)
_HpnicfMpMemberlinkTable_Object=MibTable
hpnicfMpMemberlinkTable=_HpnicfMpMemberlinkTable_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,2))
if mibBuilder.loadTexts:hpnicfMpMemberlinkTable.setStatus(_A)
_HpnicfMpMemberlinkEntry_Object=MibTableRow
hpnicfMpMemberlinkEntry=_HpnicfMpMemberlinkEntry_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,2,1))
hpnicfMpMemberlinkEntry.setIndexNames((0,_D,_E),(0,_B,_F))
if mibBuilder.loadTexts:hpnicfMpMemberlinkEntry.setStatus(_A)
_HpnicfMpMemberlinkSeqNumber_Type=Integer32
_HpnicfMpMemberlinkSeqNumber_Object=MibTableColumn
hpnicfMpMemberlinkSeqNumber=_HpnicfMpMemberlinkSeqNumber_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,2,1,1),_HpnicfMpMemberlinkSeqNumber_Type())
hpnicfMpMemberlinkSeqNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpMemberlinkSeqNumber.setStatus(_A)
_HpnicfMpMemberlinkIfIndex_Type=Integer32
_HpnicfMpMemberlinkIfIndex_Object=MibTableColumn
hpnicfMpMemberlinkIfIndex=_HpnicfMpMemberlinkIfIndex_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,2,1,2),_HpnicfMpMemberlinkIfIndex_Type())
hpnicfMpMemberlinkIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpMemberlinkIfIndex.setStatus(_A)
_HpnicfMpMemberlinkDescr_Type=DisplayString
_HpnicfMpMemberlinkDescr_Object=MibTableColumn
hpnicfMpMemberlinkDescr=_HpnicfMpMemberlinkDescr_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,2,1,3),_HpnicfMpMemberlinkDescr_Type())
hpnicfMpMemberlinkDescr.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpMemberlinkDescr.setStatus(_A)
_HpnicfMpMemberlinkMpStatus_Type=Integer32
_HpnicfMpMemberlinkMpStatus_Object=MibTableColumn
hpnicfMpMemberlinkMpStatus=_HpnicfMpMemberlinkMpStatus_Object((1,3,6,1,4,1,11,2,14,11,15,8,33,1,2,1,4),_HpnicfMpMemberlinkMpStatus_Type())
hpnicfMpMemberlinkMpStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hpnicfMpMemberlinkMpStatus.setStatus(_A)
_HpnicfMpNotifications_ObjectIdentity=ObjectIdentity
hpnicfMpNotifications=_HpnicfMpNotifications_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,33,2))
_HpnicfMpConformance_ObjectIdentity=ObjectIdentity
hpnicfMpConformance=_HpnicfMpConformance_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,33,3))
_HpnicfMpCompliances_ObjectIdentity=ObjectIdentity
hpnicfMpCompliances=_HpnicfMpCompliances_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,33,3,1))
_HpnicfMpGroups_ObjectIdentity=ObjectIdentity
hpnicfMpGroups=_HpnicfMpGroups_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,8,33,3,2))
hpnicfMpMandatoryGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,33,3,2,1))
hpnicfMpMandatoryGroup.setObjects(*((_B,_G),(_B,_F),(_B,_H)))
if mibBuilder.loadTexts:hpnicfMpMandatoryGroup.setStatus(_A)
hpnicfMpInfoGroup=ObjectGroup((1,3,6,1,4,1,11,2,14,11,15,8,33,3,2,2))
hpnicfMpInfoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_G),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S)))
if mibBuilder.loadTexts:hpnicfMpInfoGroup.setStatus(_A)
hpnicfMpCompliance=ModuleCompliance((1,3,6,1,4,1,11,2,14,11,15,8,33,3,1,1))
hpnicfMpCompliance.setObjects((_B,_T))
if mibBuilder.loadTexts:hpnicfMpCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'hpnicfMultilinkPPP':hpnicfMultilinkPPP,'hpnicfMpObjects':hpnicfMpObjects,'hpnicfMpMultilinkTable':hpnicfMpMultilinkTable,'hpnicfMpMultilinkEntry':hpnicfMpMultilinkEntry,_I:hpnicfMpMultilinkDescr,_J:hpnicfMpBundleName,_K:hpnicfMpBundledSlot,_G:hpnicfMpBundledMemberCnt,_L:hpnicfMpLostFragments,_M:hpnicfMpReorderedPkts,_N:hpnicfMpUnassignedPkts,_O:hpnicfMpInterleavedPkts,_P:hpnicfMpRcvdSequence,_Q:hpnicfMpSentSequence,'hpnicfMpMemberlinkTable':hpnicfMpMemberlinkTable,'hpnicfMpMemberlinkEntry':hpnicfMpMemberlinkEntry,_F:hpnicfMpMemberlinkSeqNumber,_H:hpnicfMpMemberlinkIfIndex,_R:hpnicfMpMemberlinkDescr,_S:hpnicfMpMemberlinkMpStatus,'hpnicfMpNotifications':hpnicfMpNotifications,'hpnicfMpConformance':hpnicfMpConformance,'hpnicfMpCompliances':hpnicfMpCompliances,'hpnicfMpCompliance':hpnicfMpCompliance,'hpnicfMpGroups':hpnicfMpGroups,_T:hpnicfMpMandatoryGroup,'hpnicfMpInfoGroup':hpnicfMpInfoGroup})