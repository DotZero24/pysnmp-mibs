_J='locIfFSIPIndex'
_I='OLD-CISCO-INTERFACES-MIB'
_H='ifIndex'
_G='IF-MIB'
_F='down'
_E='up'
_D='notAvailable'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
local,=mibBuilder.importSymbols('CISCO-SMI','local')
ifIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Linterfaces_ObjectIdentity=ObjectIdentity
linterfaces=_Linterfaces_ObjectIdentity((1,3,6,1,4,1,9,2,2))
_LifTable_Object=MibTable
lifTable=_LifTable_Object((1,3,6,1,4,1,9,2,2,1))
if mibBuilder.loadTexts:lifTable.setStatus(_A)
_LifEntry_Object=MibTableRow
lifEntry=_LifEntry_Object((1,3,6,1,4,1,9,2,2,1,1))
lifEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:lifEntry.setStatus(_A)
_LocIfHardType_Type=DisplayString
_LocIfHardType_Object=MibTableColumn
locIfHardType=_LocIfHardType_Object((1,3,6,1,4,1,9,2,2,1,1,1),_LocIfHardType_Type())
locIfHardType.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfHardType.setStatus(_A)
_LocIfLineProt_Type=Integer32
_LocIfLineProt_Object=MibTableColumn
locIfLineProt=_LocIfLineProt_Object((1,3,6,1,4,1,9,2,2,1,1,2),_LocIfLineProt_Type())
locIfLineProt.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfLineProt.setStatus(_A)
_LocIfLastIn_Type=Integer32
_LocIfLastIn_Object=MibTableColumn
locIfLastIn=_LocIfLastIn_Object((1,3,6,1,4,1,9,2,2,1,1,3),_LocIfLastIn_Type())
locIfLastIn.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfLastIn.setStatus(_A)
_LocIfLastOut_Type=Integer32
_LocIfLastOut_Object=MibTableColumn
locIfLastOut=_LocIfLastOut_Object((1,3,6,1,4,1,9,2,2,1,1,4),_LocIfLastOut_Type())
locIfLastOut.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfLastOut.setStatus(_A)
_LocIfLastOutHang_Type=Integer32
_LocIfLastOutHang_Object=MibTableColumn
locIfLastOutHang=_LocIfLastOutHang_Object((1,3,6,1,4,1,9,2,2,1,1,5),_LocIfLastOutHang_Type())
locIfLastOutHang.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfLastOutHang.setStatus(_A)
_LocIfInBitsSec_Type=Integer32
_LocIfInBitsSec_Object=MibTableColumn
locIfInBitsSec=_LocIfInBitsSec_Object((1,3,6,1,4,1,9,2,2,1,1,6),_LocIfInBitsSec_Type())
locIfInBitsSec.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInBitsSec.setStatus(_A)
_LocIfInPktsSec_Type=Integer32
_LocIfInPktsSec_Object=MibTableColumn
locIfInPktsSec=_LocIfInPktsSec_Object((1,3,6,1,4,1,9,2,2,1,1,7),_LocIfInPktsSec_Type())
locIfInPktsSec.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInPktsSec.setStatus(_A)
_LocIfOutBitsSec_Type=Integer32
_LocIfOutBitsSec_Object=MibTableColumn
locIfOutBitsSec=_LocIfOutBitsSec_Object((1,3,6,1,4,1,9,2,2,1,1,8),_LocIfOutBitsSec_Type())
locIfOutBitsSec.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfOutBitsSec.setStatus(_A)
_LocIfOutPktsSec_Type=Integer32
_LocIfOutPktsSec_Object=MibTableColumn
locIfOutPktsSec=_LocIfOutPktsSec_Object((1,3,6,1,4,1,9,2,2,1,1,9),_LocIfOutPktsSec_Type())
locIfOutPktsSec.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfOutPktsSec.setStatus(_A)
_LocIfInRunts_Type=Integer32
_LocIfInRunts_Object=MibTableColumn
locIfInRunts=_LocIfInRunts_Object((1,3,6,1,4,1,9,2,2,1,1,10),_LocIfInRunts_Type())
locIfInRunts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInRunts.setStatus(_A)
_LocIfInGiants_Type=Integer32
_LocIfInGiants_Object=MibTableColumn
locIfInGiants=_LocIfInGiants_Object((1,3,6,1,4,1,9,2,2,1,1,11),_LocIfInGiants_Type())
locIfInGiants.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInGiants.setStatus(_A)
_LocIfInCRC_Type=Integer32
_LocIfInCRC_Object=MibTableColumn
locIfInCRC=_LocIfInCRC_Object((1,3,6,1,4,1,9,2,2,1,1,12),_LocIfInCRC_Type())
locIfInCRC.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInCRC.setStatus(_A)
_LocIfInFrame_Type=Integer32
_LocIfInFrame_Object=MibTableColumn
locIfInFrame=_LocIfInFrame_Object((1,3,6,1,4,1,9,2,2,1,1,13),_LocIfInFrame_Type())
locIfInFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInFrame.setStatus(_A)
_LocIfInOverrun_Type=Integer32
_LocIfInOverrun_Object=MibTableColumn
locIfInOverrun=_LocIfInOverrun_Object((1,3,6,1,4,1,9,2,2,1,1,14),_LocIfInOverrun_Type())
locIfInOverrun.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInOverrun.setStatus(_A)
_LocIfInIgnored_Type=Integer32
_LocIfInIgnored_Object=MibTableColumn
locIfInIgnored=_LocIfInIgnored_Object((1,3,6,1,4,1,9,2,2,1,1,15),_LocIfInIgnored_Type())
locIfInIgnored.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInIgnored.setStatus(_A)
_LocIfInAbort_Type=Integer32
_LocIfInAbort_Object=MibTableColumn
locIfInAbort=_LocIfInAbort_Object((1,3,6,1,4,1,9,2,2,1,1,16),_LocIfInAbort_Type())
locIfInAbort.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInAbort.setStatus(_A)
_LocIfResets_Type=Integer32
_LocIfResets_Object=MibTableColumn
locIfResets=_LocIfResets_Object((1,3,6,1,4,1,9,2,2,1,1,17),_LocIfResets_Type())
locIfResets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfResets.setStatus(_A)
_LocIfRestarts_Type=Integer32
_LocIfRestarts_Object=MibTableColumn
locIfRestarts=_LocIfRestarts_Object((1,3,6,1,4,1,9,2,2,1,1,18),_LocIfRestarts_Type())
locIfRestarts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfRestarts.setStatus(_A)
_LocIfKeep_Type=Integer32
_LocIfKeep_Object=MibTableColumn
locIfKeep=_LocIfKeep_Object((1,3,6,1,4,1,9,2,2,1,1,19),_LocIfKeep_Type())
locIfKeep.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfKeep.setStatus(_A)
_LocIfReason_Type=DisplayString
_LocIfReason_Object=MibTableColumn
locIfReason=_LocIfReason_Object((1,3,6,1,4,1,9,2,2,1,1,20),_LocIfReason_Type())
locIfReason.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfReason.setStatus(_A)
_LocIfCarTrans_Type=Integer32
_LocIfCarTrans_Object=MibTableColumn
locIfCarTrans=_LocIfCarTrans_Object((1,3,6,1,4,1,9,2,2,1,1,21),_LocIfCarTrans_Type())
locIfCarTrans.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfCarTrans.setStatus(_A)
_LocIfReliab_Type=Integer32
_LocIfReliab_Object=MibTableColumn
locIfReliab=_LocIfReliab_Object((1,3,6,1,4,1,9,2,2,1,1,22),_LocIfReliab_Type())
locIfReliab.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfReliab.setStatus(_A)
_LocIfDelay_Type=Integer32
_LocIfDelay_Object=MibTableColumn
locIfDelay=_LocIfDelay_Object((1,3,6,1,4,1,9,2,2,1,1,23),_LocIfDelay_Type())
locIfDelay.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfDelay.setStatus(_A)
_LocIfLoad_Type=Integer32
_LocIfLoad_Object=MibTableColumn
locIfLoad=_LocIfLoad_Object((1,3,6,1,4,1,9,2,2,1,1,24),_LocIfLoad_Type())
locIfLoad.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfLoad.setStatus(_A)
_LocIfCollisions_Type=Integer32
_LocIfCollisions_Object=MibTableColumn
locIfCollisions=_LocIfCollisions_Object((1,3,6,1,4,1,9,2,2,1,1,25),_LocIfCollisions_Type())
locIfCollisions.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfCollisions.setStatus(_A)
_LocIfInputQueueDrops_Type=Integer32
_LocIfInputQueueDrops_Object=MibTableColumn
locIfInputQueueDrops=_LocIfInputQueueDrops_Object((1,3,6,1,4,1,9,2,2,1,1,26),_LocIfInputQueueDrops_Type())
locIfInputQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfInputQueueDrops.setStatus(_A)
_LocIfOutputQueueDrops_Type=Integer32
_LocIfOutputQueueDrops_Object=MibTableColumn
locIfOutputQueueDrops=_LocIfOutputQueueDrops_Object((1,3,6,1,4,1,9,2,2,1,1,27),_LocIfOutputQueueDrops_Type())
locIfOutputQueueDrops.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfOutputQueueDrops.setStatus(_A)
_LocIfDescr_Type=DisplayString
_LocIfDescr_Object=MibTableColumn
locIfDescr=_LocIfDescr_Object((1,3,6,1,4,1,9,2,2,1,1,28),_LocIfDescr_Type())
locIfDescr.setMaxAccess('read-write')
if mibBuilder.loadTexts:locIfDescr.setStatus(_A)
_LocIfSlowInPkts_Type=Counter32
_LocIfSlowInPkts_Object=MibTableColumn
locIfSlowInPkts=_LocIfSlowInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,30),_LocIfSlowInPkts_Type())
locIfSlowInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfSlowInPkts.setStatus(_A)
_LocIfSlowOutPkts_Type=Counter32
_LocIfSlowOutPkts_Object=MibTableColumn
locIfSlowOutPkts=_LocIfSlowOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,31),_LocIfSlowOutPkts_Type())
locIfSlowOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfSlowOutPkts.setStatus(_A)
_LocIfSlowInOctets_Type=Counter32
_LocIfSlowInOctets_Object=MibTableColumn
locIfSlowInOctets=_LocIfSlowInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,32),_LocIfSlowInOctets_Type())
locIfSlowInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfSlowInOctets.setStatus(_A)
_LocIfSlowOutOctets_Type=Counter32
_LocIfSlowOutOctets_Object=MibTableColumn
locIfSlowOutOctets=_LocIfSlowOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,33),_LocIfSlowOutOctets_Type())
locIfSlowOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfSlowOutOctets.setStatus(_A)
_LocIfFastInPkts_Type=Counter32
_LocIfFastInPkts_Object=MibTableColumn
locIfFastInPkts=_LocIfFastInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,34),_LocIfFastInPkts_Type())
locIfFastInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFastInPkts.setStatus(_A)
_LocIfFastOutPkts_Type=Counter32
_LocIfFastOutPkts_Object=MibTableColumn
locIfFastOutPkts=_LocIfFastOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,35),_LocIfFastOutPkts_Type())
locIfFastOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFastOutPkts.setStatus(_A)
_LocIfFastInOctets_Type=Counter32
_LocIfFastInOctets_Object=MibTableColumn
locIfFastInOctets=_LocIfFastInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,36),_LocIfFastInOctets_Type())
locIfFastInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFastInOctets.setStatus(_A)
_LocIfFastOutOctets_Type=Counter32
_LocIfFastOutOctets_Object=MibTableColumn
locIfFastOutOctets=_LocIfFastOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,37),_LocIfFastOutOctets_Type())
locIfFastOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFastOutOctets.setStatus(_A)
_LocIfotherInPkts_Type=Counter32
_LocIfotherInPkts_Object=MibTableColumn
locIfotherInPkts=_LocIfotherInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,38),_LocIfotherInPkts_Type())
locIfotherInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfotherInPkts.setStatus(_A)
_LocIfotherOutPkts_Type=Counter32
_LocIfotherOutPkts_Object=MibTableColumn
locIfotherOutPkts=_LocIfotherOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,39),_LocIfotherOutPkts_Type())
locIfotherOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfotherOutPkts.setStatus(_A)
_LocIfotherInOctets_Type=Counter32
_LocIfotherInOctets_Object=MibTableColumn
locIfotherInOctets=_LocIfotherInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,40),_LocIfotherInOctets_Type())
locIfotherInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfotherInOctets.setStatus(_A)
_LocIfotherOutOctets_Type=Counter32
_LocIfotherOutOctets_Object=MibTableColumn
locIfotherOutOctets=_LocIfotherOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,41),_LocIfotherOutOctets_Type())
locIfotherOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfotherOutOctets.setStatus(_A)
_LocIfipInPkts_Type=Counter32
_LocIfipInPkts_Object=MibTableColumn
locIfipInPkts=_LocIfipInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,42),_LocIfipInPkts_Type())
locIfipInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfipInPkts.setStatus(_A)
_LocIfipOutPkts_Type=Counter32
_LocIfipOutPkts_Object=MibTableColumn
locIfipOutPkts=_LocIfipOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,43),_LocIfipOutPkts_Type())
locIfipOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfipOutPkts.setStatus(_A)
_LocIfipInOctets_Type=Counter32
_LocIfipInOctets_Object=MibTableColumn
locIfipInOctets=_LocIfipInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,44),_LocIfipInOctets_Type())
locIfipInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfipInOctets.setStatus(_A)
_LocIfipOutOctets_Type=Counter32
_LocIfipOutOctets_Object=MibTableColumn
locIfipOutOctets=_LocIfipOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,45),_LocIfipOutOctets_Type())
locIfipOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfipOutOctets.setStatus(_A)
_LocIfdecnetInPkts_Type=Counter32
_LocIfdecnetInPkts_Object=MibTableColumn
locIfdecnetInPkts=_LocIfdecnetInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,46),_LocIfdecnetInPkts_Type())
locIfdecnetInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfdecnetInPkts.setStatus(_A)
_LocIfdecnetOutPkts_Type=Counter32
_LocIfdecnetOutPkts_Object=MibTableColumn
locIfdecnetOutPkts=_LocIfdecnetOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,47),_LocIfdecnetOutPkts_Type())
locIfdecnetOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfdecnetOutPkts.setStatus(_A)
_LocIfdecnetInOctets_Type=Counter32
_LocIfdecnetInOctets_Object=MibTableColumn
locIfdecnetInOctets=_LocIfdecnetInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,48),_LocIfdecnetInOctets_Type())
locIfdecnetInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfdecnetInOctets.setStatus(_A)
_LocIfdecnetOutOctets_Type=Counter32
_LocIfdecnetOutOctets_Object=MibTableColumn
locIfdecnetOutOctets=_LocIfdecnetOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,49),_LocIfdecnetOutOctets_Type())
locIfdecnetOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfdecnetOutOctets.setStatus(_A)
_LocIfxnsInPkts_Type=Counter32
_LocIfxnsInPkts_Object=MibTableColumn
locIfxnsInPkts=_LocIfxnsInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,50),_LocIfxnsInPkts_Type())
locIfxnsInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfxnsInPkts.setStatus(_A)
_LocIfxnsOutPkts_Type=Counter32
_LocIfxnsOutPkts_Object=MibTableColumn
locIfxnsOutPkts=_LocIfxnsOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,51),_LocIfxnsOutPkts_Type())
locIfxnsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfxnsOutPkts.setStatus(_A)
_LocIfxnsInOctets_Type=Counter32
_LocIfxnsInOctets_Object=MibTableColumn
locIfxnsInOctets=_LocIfxnsInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,52),_LocIfxnsInOctets_Type())
locIfxnsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfxnsInOctets.setStatus(_A)
_LocIfxnsOutOctets_Type=Counter32
_LocIfxnsOutOctets_Object=MibTableColumn
locIfxnsOutOctets=_LocIfxnsOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,53),_LocIfxnsOutOctets_Type())
locIfxnsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfxnsOutOctets.setStatus(_A)
_LocIfclnsInPkts_Type=Counter32
_LocIfclnsInPkts_Object=MibTableColumn
locIfclnsInPkts=_LocIfclnsInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,54),_LocIfclnsInPkts_Type())
locIfclnsInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfclnsInPkts.setStatus(_A)
_LocIfclnsOutPkts_Type=Counter32
_LocIfclnsOutPkts_Object=MibTableColumn
locIfclnsOutPkts=_LocIfclnsOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,55),_LocIfclnsOutPkts_Type())
locIfclnsOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfclnsOutPkts.setStatus(_A)
_LocIfclnsInOctets_Type=Counter32
_LocIfclnsInOctets_Object=MibTableColumn
locIfclnsInOctets=_LocIfclnsInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,56),_LocIfclnsInOctets_Type())
locIfclnsInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfclnsInOctets.setStatus(_A)
_LocIfclnsOutOctets_Type=Counter32
_LocIfclnsOutOctets_Object=MibTableColumn
locIfclnsOutOctets=_LocIfclnsOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,57),_LocIfclnsOutOctets_Type())
locIfclnsOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfclnsOutOctets.setStatus(_A)
_LocIfappletalkInPkts_Type=Counter32
_LocIfappletalkInPkts_Object=MibTableColumn
locIfappletalkInPkts=_LocIfappletalkInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,58),_LocIfappletalkInPkts_Type())
locIfappletalkInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfappletalkInPkts.setStatus(_A)
_LocIfappletalkOutPkts_Type=Counter32
_LocIfappletalkOutPkts_Object=MibTableColumn
locIfappletalkOutPkts=_LocIfappletalkOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,59),_LocIfappletalkOutPkts_Type())
locIfappletalkOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfappletalkOutPkts.setStatus(_A)
_LocIfappletalkInOctets_Type=Counter32
_LocIfappletalkInOctets_Object=MibTableColumn
locIfappletalkInOctets=_LocIfappletalkInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,60),_LocIfappletalkInOctets_Type())
locIfappletalkInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfappletalkInOctets.setStatus(_A)
_LocIfappletalkOutOctets_Type=Counter32
_LocIfappletalkOutOctets_Object=MibTableColumn
locIfappletalkOutOctets=_LocIfappletalkOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,61),_LocIfappletalkOutOctets_Type())
locIfappletalkOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfappletalkOutOctets.setStatus(_A)
_LocIfnovellInPkts_Type=Counter32
_LocIfnovellInPkts_Object=MibTableColumn
locIfnovellInPkts=_LocIfnovellInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,62),_LocIfnovellInPkts_Type())
locIfnovellInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfnovellInPkts.setStatus(_A)
_LocIfnovellOutPkts_Type=Counter32
_LocIfnovellOutPkts_Object=MibTableColumn
locIfnovellOutPkts=_LocIfnovellOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,63),_LocIfnovellOutPkts_Type())
locIfnovellOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfnovellOutPkts.setStatus(_A)
_LocIfnovellInOctets_Type=Counter32
_LocIfnovellInOctets_Object=MibTableColumn
locIfnovellInOctets=_LocIfnovellInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,64),_LocIfnovellInOctets_Type())
locIfnovellInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfnovellInOctets.setStatus(_A)
_LocIfnovellOutOctets_Type=Counter32
_LocIfnovellOutOctets_Object=MibTableColumn
locIfnovellOutOctets=_LocIfnovellOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,65),_LocIfnovellOutOctets_Type())
locIfnovellOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfnovellOutOctets.setStatus(_A)
_LocIfapolloInPkts_Type=Counter32
_LocIfapolloInPkts_Object=MibTableColumn
locIfapolloInPkts=_LocIfapolloInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,66),_LocIfapolloInPkts_Type())
locIfapolloInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfapolloInPkts.setStatus(_A)
_LocIfapolloOutPkts_Type=Counter32
_LocIfapolloOutPkts_Object=MibTableColumn
locIfapolloOutPkts=_LocIfapolloOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,67),_LocIfapolloOutPkts_Type())
locIfapolloOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfapolloOutPkts.setStatus(_A)
_LocIfapolloInOctets_Type=Counter32
_LocIfapolloInOctets_Object=MibTableColumn
locIfapolloInOctets=_LocIfapolloInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,68),_LocIfapolloInOctets_Type())
locIfapolloInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfapolloInOctets.setStatus(_A)
_LocIfapolloOutOctets_Type=Counter32
_LocIfapolloOutOctets_Object=MibTableColumn
locIfapolloOutOctets=_LocIfapolloOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,69),_LocIfapolloOutOctets_Type())
locIfapolloOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfapolloOutOctets.setStatus(_A)
_LocIfvinesInPkts_Type=Counter32
_LocIfvinesInPkts_Object=MibTableColumn
locIfvinesInPkts=_LocIfvinesInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,70),_LocIfvinesInPkts_Type())
locIfvinesInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfvinesInPkts.setStatus(_A)
_LocIfvinesOutPkts_Type=Counter32
_LocIfvinesOutPkts_Object=MibTableColumn
locIfvinesOutPkts=_LocIfvinesOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,71),_LocIfvinesOutPkts_Type())
locIfvinesOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfvinesOutPkts.setStatus(_A)
_LocIfvinesInOctets_Type=Counter32
_LocIfvinesInOctets_Object=MibTableColumn
locIfvinesInOctets=_LocIfvinesInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,72),_LocIfvinesInOctets_Type())
locIfvinesInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfvinesInOctets.setStatus(_A)
_LocIfvinesOutOctets_Type=Counter32
_LocIfvinesOutOctets_Object=MibTableColumn
locIfvinesOutOctets=_LocIfvinesOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,73),_LocIfvinesOutOctets_Type())
locIfvinesOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfvinesOutOctets.setStatus(_A)
_LocIfbridgedInPkts_Type=Counter32
_LocIfbridgedInPkts_Object=MibTableColumn
locIfbridgedInPkts=_LocIfbridgedInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,74),_LocIfbridgedInPkts_Type())
locIfbridgedInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfbridgedInPkts.setStatus(_A)
_LocIfbridgedOutPkts_Type=Counter32
_LocIfbridgedOutPkts_Object=MibTableColumn
locIfbridgedOutPkts=_LocIfbridgedOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,75),_LocIfbridgedOutPkts_Type())
locIfbridgedOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfbridgedOutPkts.setStatus(_A)
_LocIfbridgedInOctets_Type=Counter32
_LocIfbridgedInOctets_Object=MibTableColumn
locIfbridgedInOctets=_LocIfbridgedInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,76),_LocIfbridgedInOctets_Type())
locIfbridgedInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfbridgedInOctets.setStatus(_A)
_LocIfbridgedOutOctets_Type=Counter32
_LocIfbridgedOutOctets_Object=MibTableColumn
locIfbridgedOutOctets=_LocIfbridgedOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,77),_LocIfbridgedOutOctets_Type())
locIfbridgedOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfbridgedOutOctets.setStatus(_A)
_LocIfsrbInPkts_Type=Counter32
_LocIfsrbInPkts_Object=MibTableColumn
locIfsrbInPkts=_LocIfsrbInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,78),_LocIfsrbInPkts_Type())
locIfsrbInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfsrbInPkts.setStatus(_A)
_LocIfsrbOutPkts_Type=Counter32
_LocIfsrbOutPkts_Object=MibTableColumn
locIfsrbOutPkts=_LocIfsrbOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,79),_LocIfsrbOutPkts_Type())
locIfsrbOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfsrbOutPkts.setStatus(_A)
_LocIfsrbInOctets_Type=Counter32
_LocIfsrbInOctets_Object=MibTableColumn
locIfsrbInOctets=_LocIfsrbInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,80),_LocIfsrbInOctets_Type())
locIfsrbInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfsrbInOctets.setStatus(_A)
_LocIfsrbOutOctets_Type=Counter32
_LocIfsrbOutOctets_Object=MibTableColumn
locIfsrbOutOctets=_LocIfsrbOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,81),_LocIfsrbOutOctets_Type())
locIfsrbOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfsrbOutOctets.setStatus(_A)
_LocIfchaosInPkts_Type=Counter32
_LocIfchaosInPkts_Object=MibTableColumn
locIfchaosInPkts=_LocIfchaosInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,82),_LocIfchaosInPkts_Type())
locIfchaosInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfchaosInPkts.setStatus(_A)
_LocIfchaosOutPkts_Type=Counter32
_LocIfchaosOutPkts_Object=MibTableColumn
locIfchaosOutPkts=_LocIfchaosOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,83),_LocIfchaosOutPkts_Type())
locIfchaosOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfchaosOutPkts.setStatus(_A)
_LocIfchaosInOctets_Type=Counter32
_LocIfchaosInOctets_Object=MibTableColumn
locIfchaosInOctets=_LocIfchaosInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,84),_LocIfchaosInOctets_Type())
locIfchaosInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfchaosInOctets.setStatus(_A)
_LocIfchaosOutOctets_Type=Counter32
_LocIfchaosOutOctets_Object=MibTableColumn
locIfchaosOutOctets=_LocIfchaosOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,85),_LocIfchaosOutOctets_Type())
locIfchaosOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfchaosOutOctets.setStatus(_A)
_LocIfpupInPkts_Type=Counter32
_LocIfpupInPkts_Object=MibTableColumn
locIfpupInPkts=_LocIfpupInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,86),_LocIfpupInPkts_Type())
locIfpupInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfpupInPkts.setStatus(_A)
_LocIfpupOutPkts_Type=Counter32
_LocIfpupOutPkts_Object=MibTableColumn
locIfpupOutPkts=_LocIfpupOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,87),_LocIfpupOutPkts_Type())
locIfpupOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfpupOutPkts.setStatus(_A)
_LocIfpupInOctets_Type=Counter32
_LocIfpupInOctets_Object=MibTableColumn
locIfpupInOctets=_LocIfpupInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,88),_LocIfpupInOctets_Type())
locIfpupInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfpupInOctets.setStatus(_A)
_LocIfpupOutOctets_Type=Counter32
_LocIfpupOutOctets_Object=MibTableColumn
locIfpupOutOctets=_LocIfpupOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,89),_LocIfpupOutOctets_Type())
locIfpupOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfpupOutOctets.setStatus(_A)
_LocIfmopInPkts_Type=Counter32
_LocIfmopInPkts_Object=MibTableColumn
locIfmopInPkts=_LocIfmopInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,90),_LocIfmopInPkts_Type())
locIfmopInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfmopInPkts.setStatus(_A)
_LocIfmopOutPkts_Type=Counter32
_LocIfmopOutPkts_Object=MibTableColumn
locIfmopOutPkts=_LocIfmopOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,91),_LocIfmopOutPkts_Type())
locIfmopOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfmopOutPkts.setStatus(_A)
_LocIfmopInOctets_Type=Counter32
_LocIfmopInOctets_Object=MibTableColumn
locIfmopInOctets=_LocIfmopInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,92),_LocIfmopInOctets_Type())
locIfmopInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfmopInOctets.setStatus(_A)
_LocIfmopOutOctets_Type=Counter32
_LocIfmopOutOctets_Object=MibTableColumn
locIfmopOutOctets=_LocIfmopOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,93),_LocIfmopOutOctets_Type())
locIfmopOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfmopOutOctets.setStatus(_A)
_LocIflanmanInPkts_Type=Counter32
_LocIflanmanInPkts_Object=MibTableColumn
locIflanmanInPkts=_LocIflanmanInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,94),_LocIflanmanInPkts_Type())
locIflanmanInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIflanmanInPkts.setStatus(_A)
_LocIflanmanOutPkts_Type=Counter32
_LocIflanmanOutPkts_Object=MibTableColumn
locIflanmanOutPkts=_LocIflanmanOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,95),_LocIflanmanOutPkts_Type())
locIflanmanOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIflanmanOutPkts.setStatus(_A)
_LocIflanmanInOctets_Type=Counter32
_LocIflanmanInOctets_Object=MibTableColumn
locIflanmanInOctets=_LocIflanmanInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,96),_LocIflanmanInOctets_Type())
locIflanmanInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIflanmanInOctets.setStatus(_A)
_LocIflanmanOutOctets_Type=Counter32
_LocIflanmanOutOctets_Object=MibTableColumn
locIflanmanOutOctets=_LocIflanmanOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,97),_LocIflanmanOutOctets_Type())
locIflanmanOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIflanmanOutOctets.setStatus(_A)
_LocIfstunInPkts_Type=Counter32
_LocIfstunInPkts_Object=MibTableColumn
locIfstunInPkts=_LocIfstunInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,98),_LocIfstunInPkts_Type())
locIfstunInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfstunInPkts.setStatus(_A)
_LocIfstunOutPkts_Type=Counter32
_LocIfstunOutPkts_Object=MibTableColumn
locIfstunOutPkts=_LocIfstunOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,99),_LocIfstunOutPkts_Type())
locIfstunOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfstunOutPkts.setStatus(_A)
_LocIfstunInOctets_Type=Counter32
_LocIfstunInOctets_Object=MibTableColumn
locIfstunInOctets=_LocIfstunInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,100),_LocIfstunInOctets_Type())
locIfstunInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfstunInOctets.setStatus(_A)
_LocIfstunOutOctets_Type=Counter32
_LocIfstunOutOctets_Object=MibTableColumn
locIfstunOutOctets=_LocIfstunOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,101),_LocIfstunOutOctets_Type())
locIfstunOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfstunOutOctets.setStatus(_A)
_LocIfspanInPkts_Type=Counter32
_LocIfspanInPkts_Object=MibTableColumn
locIfspanInPkts=_LocIfspanInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,102),_LocIfspanInPkts_Type())
locIfspanInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfspanInPkts.setStatus(_A)
_LocIfspanOutPkts_Type=Counter32
_LocIfspanOutPkts_Object=MibTableColumn
locIfspanOutPkts=_LocIfspanOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,103),_LocIfspanOutPkts_Type())
locIfspanOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfspanOutPkts.setStatus(_A)
_LocIfspanInOctets_Type=Counter32
_LocIfspanInOctets_Object=MibTableColumn
locIfspanInOctets=_LocIfspanInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,104),_LocIfspanInOctets_Type())
locIfspanInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfspanInOctets.setStatus(_A)
_LocIfspanOutOctets_Type=Counter32
_LocIfspanOutOctets_Object=MibTableColumn
locIfspanOutOctets=_LocIfspanOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,105),_LocIfspanOutOctets_Type())
locIfspanOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfspanOutOctets.setStatus(_A)
_LocIfarpInPkts_Type=Counter32
_LocIfarpInPkts_Object=MibTableColumn
locIfarpInPkts=_LocIfarpInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,106),_LocIfarpInPkts_Type())
locIfarpInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfarpInPkts.setStatus(_A)
_LocIfarpOutPkts_Type=Counter32
_LocIfarpOutPkts_Object=MibTableColumn
locIfarpOutPkts=_LocIfarpOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,107),_LocIfarpOutPkts_Type())
locIfarpOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfarpOutPkts.setStatus(_A)
_LocIfarpInOctets_Type=Counter32
_LocIfarpInOctets_Object=MibTableColumn
locIfarpInOctets=_LocIfarpInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,108),_LocIfarpInOctets_Type())
locIfarpInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfarpInOctets.setStatus(_A)
_LocIfarpOutOctets_Type=Counter32
_LocIfarpOutOctets_Object=MibTableColumn
locIfarpOutOctets=_LocIfarpOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,109),_LocIfarpOutOctets_Type())
locIfarpOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfarpOutOctets.setStatus(_A)
_LocIfprobeInPkts_Type=Counter32
_LocIfprobeInPkts_Object=MibTableColumn
locIfprobeInPkts=_LocIfprobeInPkts_Object((1,3,6,1,4,1,9,2,2,1,1,110),_LocIfprobeInPkts_Type())
locIfprobeInPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfprobeInPkts.setStatus(_A)
_LocIfprobeOutPkts_Type=Counter32
_LocIfprobeOutPkts_Object=MibTableColumn
locIfprobeOutPkts=_LocIfprobeOutPkts_Object((1,3,6,1,4,1,9,2,2,1,1,111),_LocIfprobeOutPkts_Type())
locIfprobeOutPkts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfprobeOutPkts.setStatus(_A)
_LocIfprobeInOctets_Type=Counter32
_LocIfprobeInOctets_Object=MibTableColumn
locIfprobeInOctets=_LocIfprobeInOctets_Object((1,3,6,1,4,1,9,2,2,1,1,112),_LocIfprobeInOctets_Type())
locIfprobeInOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfprobeInOctets.setStatus(_A)
_LocIfprobeOutOctets_Type=Counter32
_LocIfprobeOutOctets_Object=MibTableColumn
locIfprobeOutOctets=_LocIfprobeOutOctets_Object((1,3,6,1,4,1,9,2,2,1,1,113),_LocIfprobeOutOctets_Type())
locIfprobeOutOctets.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfprobeOutOctets.setStatus(_A)
_LocIfDribbleInputs_Type=Counter32
_LocIfDribbleInputs_Object=MibTableColumn
locIfDribbleInputs=_LocIfDribbleInputs_Object((1,3,6,1,4,1,9,2,2,1,1,114),_LocIfDribbleInputs_Type())
locIfDribbleInputs.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfDribbleInputs.setStatus(_A)
_LFSIPTable_Object=MibTable
lFSIPTable=_LFSIPTable_Object((1,3,6,1,4,1,9,2,2,2))
if mibBuilder.loadTexts:lFSIPTable.setStatus(_A)
_LFSIPEntry_Object=MibTableRow
lFSIPEntry=_LFSIPEntry_Object((1,3,6,1,4,1,9,2,2,2,1))
lFSIPEntry.setIndexNames((0,_I,_J))
if mibBuilder.loadTexts:lFSIPEntry.setStatus(_A)
_LocIfFSIPIndex_Type=Integer32
_LocIfFSIPIndex_Object=MibTableColumn
locIfFSIPIndex=_LocIfFSIPIndex_Object((1,3,6,1,4,1,9,2,2,2,1,1),_LocIfFSIPIndex_Type())
locIfFSIPIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPIndex.setStatus(_A)
class _LocIfFSIPtype_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),('dte',2),('dce',3)))
_LocIfFSIPtype_Type.__name__=_C
_LocIfFSIPtype_Object=MibTableColumn
locIfFSIPtype=_LocIfFSIPtype_Object((1,3,6,1,4,1,9,2,2,2,1,2),_LocIfFSIPtype_Type())
locIfFSIPtype.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPtype.setStatus(_A)
class _LocIfFSIPrts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_LocIfFSIPrts_Type.__name__=_C
_LocIfFSIPrts_Object=MibTableColumn
locIfFSIPrts=_LocIfFSIPrts_Object((1,3,6,1,4,1,9,2,2,2,1,3),_LocIfFSIPrts_Type())
locIfFSIPrts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPrts.setStatus(_A)
class _LocIfFSIPcts_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_LocIfFSIPcts_Type.__name__=_C
_LocIfFSIPcts_Object=MibTableColumn
locIfFSIPcts=_LocIfFSIPcts_Object((1,3,6,1,4,1,9,2,2,2,1,4),_LocIfFSIPcts_Type())
locIfFSIPcts.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPcts.setStatus(_A)
class _LocIfFSIPdtr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_LocIfFSIPdtr_Type.__name__=_C
_LocIfFSIPdtr_Object=MibTableColumn
locIfFSIPdtr=_LocIfFSIPdtr_Object((1,3,6,1,4,1,9,2,2,2,1,5),_LocIfFSIPdtr_Type())
locIfFSIPdtr.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPdtr.setStatus(_A)
class _LocIfFSIPdcd_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_LocIfFSIPdcd_Type.__name__=_C
_LocIfFSIPdcd_Object=MibTableColumn
locIfFSIPdcd=_LocIfFSIPdcd_Object((1,3,6,1,4,1,9,2,2,2,1,6),_LocIfFSIPdcd_Type())
locIfFSIPdcd.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPdcd.setStatus(_A)
class _LocIfFSIPdsr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_D,1),(_E,2),(_F,3)))
_LocIfFSIPdsr_Type.__name__=_C
_LocIfFSIPdsr_Object=MibTableColumn
locIfFSIPdsr=_LocIfFSIPdsr_Object((1,3,6,1,4,1,9,2,2,2,1,7),_LocIfFSIPdsr_Type())
locIfFSIPdsr.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPdsr.setStatus(_A)
_LocIfFSIPrxClockrate_Type=Integer32
_LocIfFSIPrxClockrate_Object=MibTableColumn
locIfFSIPrxClockrate=_LocIfFSIPrxClockrate_Object((1,3,6,1,4,1,9,2,2,2,1,8),_LocIfFSIPrxClockrate_Type())
locIfFSIPrxClockrate.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPrxClockrate.setStatus(_A)
_LocIfFSIPrxClockrateHi_Type=Integer32
_LocIfFSIPrxClockrateHi_Object=MibTableColumn
locIfFSIPrxClockrateHi=_LocIfFSIPrxClockrateHi_Object((1,3,6,1,4,1,9,2,2,2,1,9),_LocIfFSIPrxClockrateHi_Type())
locIfFSIPrxClockrateHi.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPrxClockrateHi.setStatus(_A)
class _LocIfFSIPportType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9)));namedValues=NamedValues(*(('noCable',1),('rs232',2),('rs422',3),('rs423',4),('v35',5),('x21',6),('rs449',7),('rs530',8),('hssi',9)))
_LocIfFSIPportType_Type.__name__=_C
_LocIfFSIPportType_Object=MibTableColumn
locIfFSIPportType=_LocIfFSIPportType_Object((1,3,6,1,4,1,9,2,2,2,1,10),_LocIfFSIPportType_Type())
locIfFSIPportType.setMaxAccess(_B)
if mibBuilder.loadTexts:locIfFSIPportType.setStatus(_A)
mibBuilder.exportSymbols(_I,**{'linterfaces':linterfaces,'lifTable':lifTable,'lifEntry':lifEntry,'locIfHardType':locIfHardType,'locIfLineProt':locIfLineProt,'locIfLastIn':locIfLastIn,'locIfLastOut':locIfLastOut,'locIfLastOutHang':locIfLastOutHang,'locIfInBitsSec':locIfInBitsSec,'locIfInPktsSec':locIfInPktsSec,'locIfOutBitsSec':locIfOutBitsSec,'locIfOutPktsSec':locIfOutPktsSec,'locIfInRunts':locIfInRunts,'locIfInGiants':locIfInGiants,'locIfInCRC':locIfInCRC,'locIfInFrame':locIfInFrame,'locIfInOverrun':locIfInOverrun,'locIfInIgnored':locIfInIgnored,'locIfInAbort':locIfInAbort,'locIfResets':locIfResets,'locIfRestarts':locIfRestarts,'locIfKeep':locIfKeep,'locIfReason':locIfReason,'locIfCarTrans':locIfCarTrans,'locIfReliab':locIfReliab,'locIfDelay':locIfDelay,'locIfLoad':locIfLoad,'locIfCollisions':locIfCollisions,'locIfInputQueueDrops':locIfInputQueueDrops,'locIfOutputQueueDrops':locIfOutputQueueDrops,'locIfDescr':locIfDescr,'locIfSlowInPkts':locIfSlowInPkts,'locIfSlowOutPkts':locIfSlowOutPkts,'locIfSlowInOctets':locIfSlowInOctets,'locIfSlowOutOctets':locIfSlowOutOctets,'locIfFastInPkts':locIfFastInPkts,'locIfFastOutPkts':locIfFastOutPkts,'locIfFastInOctets':locIfFastInOctets,'locIfFastOutOctets':locIfFastOutOctets,'locIfotherInPkts':locIfotherInPkts,'locIfotherOutPkts':locIfotherOutPkts,'locIfotherInOctets':locIfotherInOctets,'locIfotherOutOctets':locIfotherOutOctets,'locIfipInPkts':locIfipInPkts,'locIfipOutPkts':locIfipOutPkts,'locIfipInOctets':locIfipInOctets,'locIfipOutOctets':locIfipOutOctets,'locIfdecnetInPkts':locIfdecnetInPkts,'locIfdecnetOutPkts':locIfdecnetOutPkts,'locIfdecnetInOctets':locIfdecnetInOctets,'locIfdecnetOutOctets':locIfdecnetOutOctets,'locIfxnsInPkts':locIfxnsInPkts,'locIfxnsOutPkts':locIfxnsOutPkts,'locIfxnsInOctets':locIfxnsInOctets,'locIfxnsOutOctets':locIfxnsOutOctets,'locIfclnsInPkts':locIfclnsInPkts,'locIfclnsOutPkts':locIfclnsOutPkts,'locIfclnsInOctets':locIfclnsInOctets,'locIfclnsOutOctets':locIfclnsOutOctets,'locIfappletalkInPkts':locIfappletalkInPkts,'locIfappletalkOutPkts':locIfappletalkOutPkts,'locIfappletalkInOctets':locIfappletalkInOctets,'locIfappletalkOutOctets':locIfappletalkOutOctets,'locIfnovellInPkts':locIfnovellInPkts,'locIfnovellOutPkts':locIfnovellOutPkts,'locIfnovellInOctets':locIfnovellInOctets,'locIfnovellOutOctets':locIfnovellOutOctets,'locIfapolloInPkts':locIfapolloInPkts,'locIfapolloOutPkts':locIfapolloOutPkts,'locIfapolloInOctets':locIfapolloInOctets,'locIfapolloOutOctets':locIfapolloOutOctets,'locIfvinesInPkts':locIfvinesInPkts,'locIfvinesOutPkts':locIfvinesOutPkts,'locIfvinesInOctets':locIfvinesInOctets,'locIfvinesOutOctets':locIfvinesOutOctets,'locIfbridgedInPkts':locIfbridgedInPkts,'locIfbridgedOutPkts':locIfbridgedOutPkts,'locIfbridgedInOctets':locIfbridgedInOctets,'locIfbridgedOutOctets':locIfbridgedOutOctets,'locIfsrbInPkts':locIfsrbInPkts,'locIfsrbOutPkts':locIfsrbOutPkts,'locIfsrbInOctets':locIfsrbInOctets,'locIfsrbOutOctets':locIfsrbOutOctets,'locIfchaosInPkts':locIfchaosInPkts,'locIfchaosOutPkts':locIfchaosOutPkts,'locIfchaosInOctets':locIfchaosInOctets,'locIfchaosOutOctets':locIfchaosOutOctets,'locIfpupInPkts':locIfpupInPkts,'locIfpupOutPkts':locIfpupOutPkts,'locIfpupInOctets':locIfpupInOctets,'locIfpupOutOctets':locIfpupOutOctets,'locIfmopInPkts':locIfmopInPkts,'locIfmopOutPkts':locIfmopOutPkts,'locIfmopInOctets':locIfmopInOctets,'locIfmopOutOctets':locIfmopOutOctets,'locIflanmanInPkts':locIflanmanInPkts,'locIflanmanOutPkts':locIflanmanOutPkts,'locIflanmanInOctets':locIflanmanInOctets,'locIflanmanOutOctets':locIflanmanOutOctets,'locIfstunInPkts':locIfstunInPkts,'locIfstunOutPkts':locIfstunOutPkts,'locIfstunInOctets':locIfstunInOctets,'locIfstunOutOctets':locIfstunOutOctets,'locIfspanInPkts':locIfspanInPkts,'locIfspanOutPkts':locIfspanOutPkts,'locIfspanInOctets':locIfspanInOctets,'locIfspanOutOctets':locIfspanOutOctets,'locIfarpInPkts':locIfarpInPkts,'locIfarpOutPkts':locIfarpOutPkts,'locIfarpInOctets':locIfarpInOctets,'locIfarpOutOctets':locIfarpOutOctets,'locIfprobeInPkts':locIfprobeInPkts,'locIfprobeOutPkts':locIfprobeOutPkts,'locIfprobeInOctets':locIfprobeInOctets,'locIfprobeOutOctets':locIfprobeOutOctets,'locIfDribbleInputs':locIfDribbleInputs,'lFSIPTable':lFSIPTable,'lFSIPEntry':lFSIPEntry,_J:locIfFSIPIndex,'locIfFSIPtype':locIfFSIPtype,'locIfFSIPrts':locIfFSIPrts,'locIfFSIPcts':locIfFSIPcts,'locIfFSIPdtr':locIfFSIPdtr,'locIfFSIPdcd':locIfFSIPdcd,'locIfFSIPdsr':locIfFSIPdsr,'locIfFSIPrxClockrate':locIfFSIPrxClockrate,'locIfFSIPrxClockrateHi':locIfFSIPrxClockrateHi,'locIfFSIPportType':locIfFSIPportType})