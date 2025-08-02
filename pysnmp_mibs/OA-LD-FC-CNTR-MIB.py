_R='oaLdFcCardPortCountersGroup'
_Q='oaLdFcCrdPrtsCntrRxBadCrcErrors'
_P='oaLdFcCrdPrtsCntrTxBadCrcErrors'
_O='oaLdFcCrdPrtsCntrRxLcvErrors'
_N='oaLdFcCrdPrtsCntrTxLcvErrors'
_M='oaLdFcCrdPrtsCntrRxTotalPckts'
_L='oaLdFcCrdPrtsCntrTxTotalPckts'
_K='oaLdFcCrdPrtsCntrRxStatus'
_J='oaLdFcCrdPrtsCntrTxStatus'
_I='noDefect'
_H='not-accessible'
_G='oaLdFcCrdPrtsCntrPortNumber'
_F='oaLdFcCrdPrtsCntrSlotNumber'
_E='Integer32'
_D='Bits'
_C='read-only'
_B='OA-LD-FC-CNTR-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI',_D,'Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
oaLdFcCntrMib=ModuleIdentity((1,3,6,1,4,1,6926,1,41,82))
if mibBuilder.loadTexts:oaLdFcCntrMib.setRevisions(('2012-07-30 00:00',))
_Oaccess_ObjectIdentity=ObjectIdentity
oaccess=_Oaccess_ObjectIdentity((1,3,6,1,4,1,6926))
_OaManagement_ObjectIdentity=ObjectIdentity
oaManagement=_OaManagement_ObjectIdentity((1,3,6,1,4,1,6926,1))
_OaLambdaDriver_ObjectIdentity=ObjectIdentity
oaLambdaDriver=_OaLambdaDriver_ObjectIdentity((1,3,6,1,4,1,6926,1,41))
_OaLdFcCardPortCounters_ObjectIdentity=ObjectIdentity
oaLdFcCardPortCounters=_OaLdFcCardPortCounters_ObjectIdentity((1,3,6,1,4,1,6926,1,41,82,1))
_OaLdFcCardPortsCntrTable_Object=MibTable
oaLdFcCardPortsCntrTable=_OaLdFcCardPortsCntrTable_Object((1,3,6,1,4,1,6926,1,41,82,1,2))
if mibBuilder.loadTexts:oaLdFcCardPortsCntrTable.setStatus(_A)
_OaLdFcCardPortsCntrEntry_Object=MibTableRow
oaLdFcCardPortsCntrEntry=_OaLdFcCardPortsCntrEntry_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1))
oaLdFcCardPortsCntrEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:oaLdFcCardPortsCntrEntry.setStatus(_A)
class _OaLdFcCrdPrtsCntrSlotNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaLdFcCrdPrtsCntrSlotNumber_Type.__name__=_E
_OaLdFcCrdPrtsCntrSlotNumber_Object=MibTableColumn
oaLdFcCrdPrtsCntrSlotNumber=_OaLdFcCrdPrtsCntrSlotNumber_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,1),_OaLdFcCrdPrtsCntrSlotNumber_Type())
oaLdFcCrdPrtsCntrSlotNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrSlotNumber.setStatus(_A)
class _OaLdFcCrdPrtsCntrPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,255))
_OaLdFcCrdPrtsCntrPortNumber_Type.__name__=_E
_OaLdFcCrdPrtsCntrPortNumber_Object=MibTableColumn
oaLdFcCrdPrtsCntrPortNumber=_OaLdFcCrdPrtsCntrPortNumber_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,2),_OaLdFcCrdPrtsCntrPortNumber_Type())
oaLdFcCrdPrtsCntrPortNumber.setMaxAccess(_H)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrPortNumber.setStatus(_A)
class _OaLdFcCrdPrtsCntrTxStatus_Type(Bits):namedValues=NamedValues(*((_I,0),('txNoSync',1),('txDLOL',2)))
_OaLdFcCrdPrtsCntrTxStatus_Type.__name__=_D
_OaLdFcCrdPrtsCntrTxStatus_Object=MibTableColumn
oaLdFcCrdPrtsCntrTxStatus=_OaLdFcCrdPrtsCntrTxStatus_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,3),_OaLdFcCrdPrtsCntrTxStatus_Type())
oaLdFcCrdPrtsCntrTxStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrTxStatus.setStatus(_A)
class _OaLdFcCrdPrtsCntrRxStatus_Type(Bits):namedValues=NamedValues(*((_I,0),('rxNoSync',1),('rxDLOL',2),('rxASD',3)))
_OaLdFcCrdPrtsCntrRxStatus_Type.__name__=_D
_OaLdFcCrdPrtsCntrRxStatus_Object=MibTableColumn
oaLdFcCrdPrtsCntrRxStatus=_OaLdFcCrdPrtsCntrRxStatus_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,4),_OaLdFcCrdPrtsCntrRxStatus_Type())
oaLdFcCrdPrtsCntrRxStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrRxStatus.setStatus(_A)
_OaLdFcCrdPrtsCntrTxTotalPckts_Type=Counter32
_OaLdFcCrdPrtsCntrTxTotalPckts_Object=MibTableColumn
oaLdFcCrdPrtsCntrTxTotalPckts=_OaLdFcCrdPrtsCntrTxTotalPckts_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,5),_OaLdFcCrdPrtsCntrTxTotalPckts_Type())
oaLdFcCrdPrtsCntrTxTotalPckts.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrTxTotalPckts.setStatus(_A)
_OaLdFcCrdPrtsCntrRxTotalPckts_Type=Counter32
_OaLdFcCrdPrtsCntrRxTotalPckts_Object=MibTableColumn
oaLdFcCrdPrtsCntrRxTotalPckts=_OaLdFcCrdPrtsCntrRxTotalPckts_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,6),_OaLdFcCrdPrtsCntrRxTotalPckts_Type())
oaLdFcCrdPrtsCntrRxTotalPckts.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrRxTotalPckts.setStatus(_A)
_OaLdFcCrdPrtsCntrTxLcvErrors_Type=Counter32
_OaLdFcCrdPrtsCntrTxLcvErrors_Object=MibTableColumn
oaLdFcCrdPrtsCntrTxLcvErrors=_OaLdFcCrdPrtsCntrTxLcvErrors_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,7),_OaLdFcCrdPrtsCntrTxLcvErrors_Type())
oaLdFcCrdPrtsCntrTxLcvErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrTxLcvErrors.setStatus(_A)
_OaLdFcCrdPrtsCntrRxLcvErrors_Type=Counter32
_OaLdFcCrdPrtsCntrRxLcvErrors_Object=MibTableColumn
oaLdFcCrdPrtsCntrRxLcvErrors=_OaLdFcCrdPrtsCntrRxLcvErrors_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,8),_OaLdFcCrdPrtsCntrRxLcvErrors_Type())
oaLdFcCrdPrtsCntrRxLcvErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrRxLcvErrors.setStatus(_A)
_OaLdFcCrdPrtsCntrTxBadCrcErrors_Type=Counter32
_OaLdFcCrdPrtsCntrTxBadCrcErrors_Object=MibTableColumn
oaLdFcCrdPrtsCntrTxBadCrcErrors=_OaLdFcCrdPrtsCntrTxBadCrcErrors_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,9),_OaLdFcCrdPrtsCntrTxBadCrcErrors_Type())
oaLdFcCrdPrtsCntrTxBadCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrTxBadCrcErrors.setStatus(_A)
_OaLdFcCrdPrtsCntrRxBadCrcErrors_Type=Counter32
_OaLdFcCrdPrtsCntrRxBadCrcErrors_Object=MibTableColumn
oaLdFcCrdPrtsCntrRxBadCrcErrors=_OaLdFcCrdPrtsCntrRxBadCrcErrors_Object((1,3,6,1,4,1,6926,1,41,82,1,2,1,10),_OaLdFcCrdPrtsCntrRxBadCrcErrors_Type())
oaLdFcCrdPrtsCntrRxBadCrcErrors.setMaxAccess(_C)
if mibBuilder.loadTexts:oaLdFcCrdPrtsCntrRxBadCrcErrors.setStatus(_A)
_OaLdFcConformance_ObjectIdentity=ObjectIdentity
oaLdFcConformance=_OaLdFcConformance_ObjectIdentity((1,3,6,1,4,1,6926,1,41,82,2))
_OaLdFcGroups_ObjectIdentity=ObjectIdentity
oaLdFcGroups=_OaLdFcGroups_ObjectIdentity((1,3,6,1,4,1,6926,1,41,82,2,1))
_OaLdFcCompliances_ObjectIdentity=ObjectIdentity
oaLdFcCompliances=_OaLdFcCompliances_ObjectIdentity((1,3,6,1,4,1,6926,1,41,82,2,2))
oaLdFcCardPortCountersGroup=ObjectGroup((1,3,6,1,4,1,6926,1,41,82,2,1,1))
oaLdFcCardPortCountersGroup.setObjects(*((_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:oaLdFcCardPortCountersGroup.setStatus(_A)
oaLdFcCompliance=ModuleCompliance((1,3,6,1,4,1,6926,1,41,82,2,2,1))
oaLdFcCompliance.setObjects((_B,_R))
if mibBuilder.loadTexts:oaLdFcCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'oaccess':oaccess,'oaManagement':oaManagement,'oaLambdaDriver':oaLambdaDriver,'oaLdFcCntrMib':oaLdFcCntrMib,'oaLdFcCardPortCounters':oaLdFcCardPortCounters,'oaLdFcCardPortsCntrTable':oaLdFcCardPortsCntrTable,'oaLdFcCardPortsCntrEntry':oaLdFcCardPortsCntrEntry,_F:oaLdFcCrdPrtsCntrSlotNumber,_G:oaLdFcCrdPrtsCntrPortNumber,_J:oaLdFcCrdPrtsCntrTxStatus,_K:oaLdFcCrdPrtsCntrRxStatus,_L:oaLdFcCrdPrtsCntrTxTotalPckts,_M:oaLdFcCrdPrtsCntrRxTotalPckts,_N:oaLdFcCrdPrtsCntrTxLcvErrors,_O:oaLdFcCrdPrtsCntrRxLcvErrors,_P:oaLdFcCrdPrtsCntrTxBadCrcErrors,_Q:oaLdFcCrdPrtsCntrRxBadCrcErrors,'oaLdFcConformance':oaLdFcConformance,'oaLdFcGroups':oaLdFcGroups,_R:oaLdFcCardPortCountersGroup,'oaLdFcCompliances':oaLdFcCompliances,'oaLdFcCompliance':oaLdFcCompliance})