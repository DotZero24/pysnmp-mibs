_O='pdnHdlcStatsTotalGroup'
_N='pdnHdlcStatsTotalTxBufUnderrun'
_M='pdnHdlcStatsTotalTx'
_L='pdnHdlcStatsTotalRxMaxSizeExceeded'
_K='pdnHdlcStatsTotalReceiverOverrun'
_J='pdnHdlcStatsTotalRxNoBufAvail'
_I='pdnHdlcStatsTotalRxBadAddress'
_H='pdnHdlcStatsTotalRxAborts'
_G='pdnHdlcStatsTotalRxCRCErrors'
_F='pdnHdlcStatsTotalRxGood'
_E='ifIndex'
_D='IF-MIB'
_C='read-only'
_B='PDN-HDLC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_D,_E)
pdn_interfaces,=mibBuilder.importSymbols('PDN-HEADER-MIB','pdn-interfaces')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
pdnHdlcMIB=ModuleIdentity((1,3,6,1,4,1,1795,2,24,2,6,26))
if mibBuilder.loadTexts:pdnHdlcMIB.setRevisions(('2004-09-10 00:00',))
_PdnHdlcNotifications_ObjectIdentity=ObjectIdentity
pdnHdlcNotifications=_PdnHdlcNotifications_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,0))
_PdnHdlcObjects_ObjectIdentity=ObjectIdentity
pdnHdlcObjects=_PdnHdlcObjects_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,1))
_PdnHdlcStatsTotalTable_Object=MibTable
pdnHdlcStatsTotalTable=_PdnHdlcStatsTotalTable_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1))
if mibBuilder.loadTexts:pdnHdlcStatsTotalTable.setStatus(_A)
_PdnHdlcStatsTotalEntry_Object=MibTableRow
pdnHdlcStatsTotalEntry=_PdnHdlcStatsTotalEntry_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1))
pdnHdlcStatsTotalEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:pdnHdlcStatsTotalEntry.setStatus(_A)
_PdnHdlcStatsTotalRxGood_Type=Counter32
_PdnHdlcStatsTotalRxGood_Object=MibTableColumn
pdnHdlcStatsTotalRxGood=_PdnHdlcStatsTotalRxGood_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,1),_PdnHdlcStatsTotalRxGood_Type())
pdnHdlcStatsTotalRxGood.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalRxGood.setStatus(_A)
_PdnHdlcStatsTotalRxCRCErrors_Type=Counter32
_PdnHdlcStatsTotalRxCRCErrors_Object=MibTableColumn
pdnHdlcStatsTotalRxCRCErrors=_PdnHdlcStatsTotalRxCRCErrors_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,2),_PdnHdlcStatsTotalRxCRCErrors_Type())
pdnHdlcStatsTotalRxCRCErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalRxCRCErrors.setStatus(_A)
_PdnHdlcStatsTotalRxAborts_Type=Counter32
_PdnHdlcStatsTotalRxAborts_Object=MibTableColumn
pdnHdlcStatsTotalRxAborts=_PdnHdlcStatsTotalRxAborts_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,3),_PdnHdlcStatsTotalRxAborts_Type())
pdnHdlcStatsTotalRxAborts.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalRxAborts.setStatus(_A)
_PdnHdlcStatsTotalRxBadAddress_Type=Counter32
_PdnHdlcStatsTotalRxBadAddress_Object=MibTableColumn
pdnHdlcStatsTotalRxBadAddress=_PdnHdlcStatsTotalRxBadAddress_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,4),_PdnHdlcStatsTotalRxBadAddress_Type())
pdnHdlcStatsTotalRxBadAddress.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalRxBadAddress.setStatus(_A)
_PdnHdlcStatsTotalRxNoBufAvail_Type=Counter32
_PdnHdlcStatsTotalRxNoBufAvail_Object=MibTableColumn
pdnHdlcStatsTotalRxNoBufAvail=_PdnHdlcStatsTotalRxNoBufAvail_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,5),_PdnHdlcStatsTotalRxNoBufAvail_Type())
pdnHdlcStatsTotalRxNoBufAvail.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalRxNoBufAvail.setStatus(_A)
_PdnHdlcStatsTotalReceiverOverrun_Type=Counter32
_PdnHdlcStatsTotalReceiverOverrun_Object=MibTableColumn
pdnHdlcStatsTotalReceiverOverrun=_PdnHdlcStatsTotalReceiverOverrun_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,6),_PdnHdlcStatsTotalReceiverOverrun_Type())
pdnHdlcStatsTotalReceiverOverrun.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalReceiverOverrun.setStatus(_A)
_PdnHdlcStatsTotalRxMaxSizeExceeded_Type=Counter32
_PdnHdlcStatsTotalRxMaxSizeExceeded_Object=MibTableColumn
pdnHdlcStatsTotalRxMaxSizeExceeded=_PdnHdlcStatsTotalRxMaxSizeExceeded_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,7),_PdnHdlcStatsTotalRxMaxSizeExceeded_Type())
pdnHdlcStatsTotalRxMaxSizeExceeded.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalRxMaxSizeExceeded.setStatus(_A)
_PdnHdlcStatsTotalTx_Type=Counter32
_PdnHdlcStatsTotalTx_Object=MibTableColumn
pdnHdlcStatsTotalTx=_PdnHdlcStatsTotalTx_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,8),_PdnHdlcStatsTotalTx_Type())
pdnHdlcStatsTotalTx.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalTx.setStatus(_A)
_PdnHdlcStatsTotalTxBufUnderrun_Type=Counter32
_PdnHdlcStatsTotalTxBufUnderrun_Object=MibTableColumn
pdnHdlcStatsTotalTxBufUnderrun=_PdnHdlcStatsTotalTxBufUnderrun_Object((1,3,6,1,4,1,1795,2,24,2,6,26,1,1,1,9),_PdnHdlcStatsTotalTxBufUnderrun_Type())
pdnHdlcStatsTotalTxBufUnderrun.setMaxAccess(_C)
if mibBuilder.loadTexts:pdnHdlcStatsTotalTxBufUnderrun.setStatus(_A)
_PdnHdlcAFNs_ObjectIdentity=ObjectIdentity
pdnHdlcAFNs=_PdnHdlcAFNs_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,2))
_PdnHdlcConformance_ObjectIdentity=ObjectIdentity
pdnHdlcConformance=_PdnHdlcConformance_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,3))
_PdnHdlcCompliances_ObjectIdentity=ObjectIdentity
pdnHdlcCompliances=_PdnHdlcCompliances_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,3,1))
_PdnHdlcGroups_ObjectIdentity=ObjectIdentity
pdnHdlcGroups=_PdnHdlcGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,3,2))
_PdnHdlcObjGroups_ObjectIdentity=ObjectIdentity
pdnHdlcObjGroups=_PdnHdlcObjGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,3,2,1))
_PdnHdlcAfnGroups_ObjectIdentity=ObjectIdentity
pdnHdlcAfnGroups=_PdnHdlcAfnGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,3,2,2))
_PdnHdlcNtfyGroups_ObjectIdentity=ObjectIdentity
pdnHdlcNtfyGroups=_PdnHdlcNtfyGroups_ObjectIdentity((1,3,6,1,4,1,1795,2,24,2,6,26,3,2,3))
pdnHdlcStatsTotalGroup=ObjectGroup((1,3,6,1,4,1,1795,2,24,2,6,26,3,2,1,1))
pdnHdlcStatsTotalGroup.setObjects(*((_B,_F),(_B,_G),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:pdnHdlcStatsTotalGroup.setStatus(_A)
pdnHdlcCompliance=ModuleCompliance((1,3,6,1,4,1,1795,2,24,2,6,26,3,1,1))
pdnHdlcCompliance.setObjects((_B,_O))
if mibBuilder.loadTexts:pdnHdlcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'pdnHdlcMIB':pdnHdlcMIB,'pdnHdlcNotifications':pdnHdlcNotifications,'pdnHdlcObjects':pdnHdlcObjects,'pdnHdlcStatsTotalTable':pdnHdlcStatsTotalTable,'pdnHdlcStatsTotalEntry':pdnHdlcStatsTotalEntry,_F:pdnHdlcStatsTotalRxGood,_G:pdnHdlcStatsTotalRxCRCErrors,_H:pdnHdlcStatsTotalRxAborts,_I:pdnHdlcStatsTotalRxBadAddress,_J:pdnHdlcStatsTotalRxNoBufAvail,_K:pdnHdlcStatsTotalReceiverOverrun,_L:pdnHdlcStatsTotalRxMaxSizeExceeded,_M:pdnHdlcStatsTotalTx,_N:pdnHdlcStatsTotalTxBufUnderrun,'pdnHdlcAFNs':pdnHdlcAFNs,'pdnHdlcConformance':pdnHdlcConformance,'pdnHdlcCompliances':pdnHdlcCompliances,'pdnHdlcCompliance':pdnHdlcCompliance,'pdnHdlcGroups':pdnHdlcGroups,'pdnHdlcObjGroups':pdnHdlcObjGroups,_O:pdnHdlcStatsTotalGroup,'pdnHdlcAfnGroups':pdnHdlcAfnGroups,'pdnHdlcNtfyGroups':pdnHdlcNtfyGroups})