_R='ciscoVismHdlcGroup'
_Q='vismHdlcMaxFrameSize'
_P='vismHdlcRxAbortFrames'
_O='vismHdlcTxAbortFrames'
_N='vismHdlcTxUnderflows'
_M='vismHdlcRcvBufOverflows'
_L='vismHdlcRcvCrcErrors'
_K='vismHdlcRcvFrames'
_J='vismHdlcXmtFrames'
_I='vismHdlcLcnNum'
_H='vismHdlcRowStatus'
_G='deprecated'
_F='read-create'
_E='vismHdlcChanNum'
_D='Integer32'
_C='read-only'
_B='CISCO-VISM-HDLC-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
voice,=mibBuilder.importSymbols('BASIS-MIB','voice')
ciscoWan,=mibBuilder.importSymbols('CISCOWAN-SMI','ciscoWan')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
ciscoVismHdlcMIB=ModuleIdentity((1,3,6,1,4,1,351,150,91))
if mibBuilder.loadTexts:ciscoVismHdlcMIB.setRevisions(('2003-10-09 00:00',))
_VismSigGrp_ObjectIdentity=ObjectIdentity
vismSigGrp=_VismSigGrp_ObjectIdentity((1,3,6,1,4,1,351,110,5,5,6))
_VismHdlcChanTable_Object=MibTable
vismHdlcChanTable=_VismHdlcChanTable_Object((1,3,6,1,4,1,351,110,5,5,6,1))
if mibBuilder.loadTexts:vismHdlcChanTable.setStatus(_A)
_VismHdlcChanEntry_Object=MibTableRow
vismHdlcChanEntry=_VismHdlcChanEntry_Object((1,3,6,1,4,1,351,110,5,5,6,1,1))
vismHdlcChanEntry.setIndexNames((0,_B,_E))
if mibBuilder.loadTexts:vismHdlcChanEntry.setStatus(_A)
class _VismHdlcChanNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,248))
_VismHdlcChanNum_Type.__name__=_D
_VismHdlcChanNum_Object=MibTableColumn
vismHdlcChanNum=_VismHdlcChanNum_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,1),_VismHdlcChanNum_Type())
vismHdlcChanNum.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcChanNum.setStatus(_A)
_VismHdlcRowStatus_Type=RowStatus
_VismHdlcRowStatus_Object=MibTableColumn
vismHdlcRowStatus=_VismHdlcRowStatus_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,2),_VismHdlcRowStatus_Type())
vismHdlcRowStatus.setMaxAccess(_F)
if mibBuilder.loadTexts:vismHdlcRowStatus.setStatus(_A)
class _VismHdlcMaxFrameSize_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_VismHdlcMaxFrameSize_Type.__name__=_D
_VismHdlcMaxFrameSize_Object=MibTableColumn
vismHdlcMaxFrameSize=_VismHdlcMaxFrameSize_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,3),_VismHdlcMaxFrameSize_Type())
vismHdlcMaxFrameSize.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcMaxFrameSize.setStatus(_G)
class _VismHdlcLcnNum_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(131,510))
_VismHdlcLcnNum_Type.__name__=_D
_VismHdlcLcnNum_Object=MibTableColumn
vismHdlcLcnNum=_VismHdlcLcnNum_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,4),_VismHdlcLcnNum_Type())
vismHdlcLcnNum.setMaxAccess(_F)
if mibBuilder.loadTexts:vismHdlcLcnNum.setStatus(_A)
_VismHdlcXmtFrames_Type=Counter32
_VismHdlcXmtFrames_Object=MibTableColumn
vismHdlcXmtFrames=_VismHdlcXmtFrames_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,5),_VismHdlcXmtFrames_Type())
vismHdlcXmtFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcXmtFrames.setStatus(_A)
_VismHdlcRcvFrames_Type=Counter32
_VismHdlcRcvFrames_Object=MibTableColumn
vismHdlcRcvFrames=_VismHdlcRcvFrames_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,6),_VismHdlcRcvFrames_Type())
vismHdlcRcvFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcRcvFrames.setStatus(_A)
_VismHdlcRcvCrcErrors_Type=Counter32
_VismHdlcRcvCrcErrors_Object=MibTableColumn
vismHdlcRcvCrcErrors=_VismHdlcRcvCrcErrors_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,7),_VismHdlcRcvCrcErrors_Type())
vismHdlcRcvCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcRcvCrcErrors.setStatus(_A)
_VismHdlcRcvBufOverflows_Type=Counter32
_VismHdlcRcvBufOverflows_Object=MibTableColumn
vismHdlcRcvBufOverflows=_VismHdlcRcvBufOverflows_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,8),_VismHdlcRcvBufOverflows_Type())
vismHdlcRcvBufOverflows.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcRcvBufOverflows.setStatus(_A)
_VismHdlcTxUnderflows_Type=Counter32
_VismHdlcTxUnderflows_Object=MibTableColumn
vismHdlcTxUnderflows=_VismHdlcTxUnderflows_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,9),_VismHdlcTxUnderflows_Type())
vismHdlcTxUnderflows.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcTxUnderflows.setStatus(_A)
_VismHdlcTxAbortFrames_Type=Counter32
_VismHdlcTxAbortFrames_Object=MibTableColumn
vismHdlcTxAbortFrames=_VismHdlcTxAbortFrames_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,10),_VismHdlcTxAbortFrames_Type())
vismHdlcTxAbortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcTxAbortFrames.setStatus(_A)
_VismHdlcRxAbortFrames_Type=Counter32
_VismHdlcRxAbortFrames_Object=MibTableColumn
vismHdlcRxAbortFrames=_VismHdlcRxAbortFrames_Object((1,3,6,1,4,1,351,110,5,5,6,1,1,11),_VismHdlcRxAbortFrames_Type())
vismHdlcRxAbortFrames.setMaxAccess(_C)
if mibBuilder.loadTexts:vismHdlcRxAbortFrames.setStatus(_A)
_CiscoVismHdlcMIBConformance_ObjectIdentity=ObjectIdentity
ciscoVismHdlcMIBConformance=_CiscoVismHdlcMIBConformance_ObjectIdentity((1,3,6,1,4,1,351,150,91,2))
_CiscoVismHdlcMIBGroups_ObjectIdentity=ObjectIdentity
ciscoVismHdlcMIBGroups=_CiscoVismHdlcMIBGroups_ObjectIdentity((1,3,6,1,4,1,351,150,91,2,1))
_CiscoVismHdlcMIBCompliances_ObjectIdentity=ObjectIdentity
ciscoVismHdlcMIBCompliances=_CiscoVismHdlcMIBCompliances_ObjectIdentity((1,3,6,1,4,1,351,150,91,2,2))
ciscoVismHdlcGroup=ObjectGroup((1,3,6,1,4,1,351,150,91,2,1,1))
ciscoVismHdlcGroup.setObjects(*((_B,_E),(_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:ciscoVismHdlcGroup.setStatus(_A)
ciscoVismHdlcDeprecateGroup=ObjectGroup((1,3,6,1,4,1,351,150,91,2,1,2))
ciscoVismHdlcDeprecateGroup.setObjects((_B,_Q))
if mibBuilder.loadTexts:ciscoVismHdlcDeprecateGroup.setStatus(_G)
ciscoVismHdlcCompliance=ModuleCompliance((1,3,6,1,4,1,351,150,91,2,2,1))
ciscoVismHdlcCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:ciscoVismHdlcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'vismSigGrp':vismSigGrp,'vismHdlcChanTable':vismHdlcChanTable,'vismHdlcChanEntry':vismHdlcChanEntry,_E:vismHdlcChanNum,_H:vismHdlcRowStatus,_Q:vismHdlcMaxFrameSize,_I:vismHdlcLcnNum,_J:vismHdlcXmtFrames,_K:vismHdlcRcvFrames,_L:vismHdlcRcvCrcErrors,_M:vismHdlcRcvBufOverflows,_N:vismHdlcTxUnderflows,_O:vismHdlcTxAbortFrames,_P:vismHdlcRxAbortFrames,'ciscoVismHdlcMIB':ciscoVismHdlcMIB,'ciscoVismHdlcMIBConformance':ciscoVismHdlcMIBConformance,'ciscoVismHdlcMIBGroups':ciscoVismHdlcMIBGroups,_R:ciscoVismHdlcGroup,'ciscoVismHdlcDeprecateGroup':ciscoVismHdlcDeprecateGroup,'ciscoVismHdlcMIBCompliances':ciscoVismHdlcMIBCompliances,'ciscoVismHdlcCompliance':ciscoVismHdlcCompliance})