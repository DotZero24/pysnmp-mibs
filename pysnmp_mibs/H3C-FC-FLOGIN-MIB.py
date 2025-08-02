_H='h3cFcFLoginIndex'
_G='H3C-FC-FLOGIN-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='h3cVsanIndex'
_C='H3C-VSAN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
H3cFcAddressId,H3cFcBbCredit,H3cFcClassOfServices,H3cFcNameId,H3cFcRxMTU=mibBuilder.importSymbols('H3C-FC-TC-MIB','H3cFcAddressId','H3cFcBbCredit','H3cFcClassOfServices','H3cFcNameId','H3cFcRxMTU')
h3cSan,h3cVsanIndex=mibBuilder.importSymbols(_C,'h3cSan',_D)
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
h3cFcFLogin=ModuleIdentity((1,3,6,1,4,1,2011,10,2,127,3))
if mibBuilder.loadTexts:h3cFcFLogin.setRevisions(('2013-02-27 11:00',))
_H3cFcFLoginMibObjects_ObjectIdentity=ObjectIdentity
h3cFcFLoginMibObjects=_H3cFcFLoginMibObjects_ObjectIdentity((1,3,6,1,4,1,2011,10,2,127,3,1))
_H3cFcFLoginTable_Object=MibTable
h3cFcFLoginTable=_H3cFcFLoginTable_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1))
if mibBuilder.loadTexts:h3cFcFLoginTable.setStatus(_A)
_H3cFcFLoginEntry_Object=MibTableRow
h3cFcFLoginEntry=_H3cFcFLoginEntry_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1))
h3cFcFLoginEntry.setIndexNames((0,_E,_F),(0,_C,_D),(0,_G,_H))
if mibBuilder.loadTexts:h3cFcFLoginEntry.setStatus(_A)
_H3cFcFLoginIndex_Type=H3cFcAddressId
_H3cFcFLoginIndex_Object=MibTableColumn
h3cFcFLoginIndex=_H3cFcFLoginIndex_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,1),_H3cFcFLoginIndex_Type())
h3cFcFLoginIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:h3cFcFLoginIndex.setStatus(_A)
_H3cFcFLoginPortNodeWWN_Type=H3cFcNameId
_H3cFcFLoginPortNodeWWN_Object=MibTableColumn
h3cFcFLoginPortNodeWWN=_H3cFcFLoginPortNodeWWN_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,2),_H3cFcFLoginPortNodeWWN_Type())
h3cFcFLoginPortNodeWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginPortNodeWWN.setStatus(_A)
_H3cFcFLoginPortWWN_Type=H3cFcNameId
_H3cFcFLoginPortWWN_Object=MibTableColumn
h3cFcFLoginPortWWN=_H3cFcFLoginPortWWN_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,3),_H3cFcFLoginPortWWN_Type())
h3cFcFLoginPortWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginPortWWN.setStatus(_A)
_H3cFcFLoginPortFcId_Type=H3cFcAddressId
_H3cFcFLoginPortFcId_Object=MibTableColumn
h3cFcFLoginPortFcId=_H3cFcFLoginPortFcId_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,4),_H3cFcFLoginPortFcId_Type())
h3cFcFLoginPortFcId.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginPortFcId.setStatus(_A)
_H3cFcFLoginRxBbCredit_Type=H3cFcBbCredit
_H3cFcFLoginRxBbCredit_Object=MibTableColumn
h3cFcFLoginRxBbCredit=_H3cFcFLoginRxBbCredit_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,5),_H3cFcFLoginRxBbCredit_Type())
h3cFcFLoginRxBbCredit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginRxBbCredit.setStatus(_A)
_H3cFcFLoginTxBbCredit_Type=H3cFcBbCredit
_H3cFcFLoginTxBbCredit_Object=MibTableColumn
h3cFcFLoginTxBbCredit=_H3cFcFLoginTxBbCredit_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,6),_H3cFcFLoginTxBbCredit_Type())
h3cFcFLoginTxBbCredit.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginTxBbCredit.setStatus(_A)
_H3cFcFLoginClass2RxMTU_Type=H3cFcRxMTU
_H3cFcFLoginClass2RxMTU_Object=MibTableColumn
h3cFcFLoginClass2RxMTU=_H3cFcFLoginClass2RxMTU_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,7),_H3cFcFLoginClass2RxMTU_Type())
h3cFcFLoginClass2RxMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginClass2RxMTU.setStatus(_A)
_H3cFcFLoginClass3RxMTU_Type=H3cFcRxMTU
_H3cFcFLoginClass3RxMTU_Object=MibTableColumn
h3cFcFLoginClass3RxMTU=_H3cFcFLoginClass3RxMTU_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,8),_H3cFcFLoginClass3RxMTU_Type())
h3cFcFLoginClass3RxMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginClass3RxMTU.setStatus(_A)
_H3cFcFLoginSuppClassRequested_Type=H3cFcClassOfServices
_H3cFcFLoginSuppClassRequested_Object=MibTableColumn
h3cFcFLoginSuppClassRequested=_H3cFcFLoginSuppClassRequested_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,9),_H3cFcFLoginSuppClassRequested_Type())
h3cFcFLoginSuppClassRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginSuppClassRequested.setStatus(_A)
_H3cFcFLoginClass2ReqAgreed_Type=TruthValue
_H3cFcFLoginClass2ReqAgreed_Object=MibTableColumn
h3cFcFLoginClass2ReqAgreed=_H3cFcFLoginClass2ReqAgreed_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,10),_H3cFcFLoginClass2ReqAgreed_Type())
h3cFcFLoginClass2ReqAgreed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginClass2ReqAgreed.setStatus(_A)
_H3cFcFLoginClass3ReqAgreed_Type=TruthValue
_H3cFcFLoginClass3ReqAgreed_Object=MibTableColumn
h3cFcFLoginClass3ReqAgreed=_H3cFcFLoginClass3ReqAgreed_Object((1,3,6,1,4,1,2011,10,2,127,3,1,1,1,11),_H3cFcFLoginClass3ReqAgreed_Type())
h3cFcFLoginClass3ReqAgreed.setMaxAccess(_B)
if mibBuilder.loadTexts:h3cFcFLoginClass3ReqAgreed.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'h3cFcFLogin':h3cFcFLogin,'h3cFcFLoginMibObjects':h3cFcFLoginMibObjects,'h3cFcFLoginTable':h3cFcFLoginTable,'h3cFcFLoginEntry':h3cFcFLoginEntry,_H:h3cFcFLoginIndex,'h3cFcFLoginPortNodeWWN':h3cFcFLoginPortNodeWWN,'h3cFcFLoginPortWWN':h3cFcFLoginPortWWN,'h3cFcFLoginPortFcId':h3cFcFLoginPortFcId,'h3cFcFLoginRxBbCredit':h3cFcFLoginRxBbCredit,'h3cFcFLoginTxBbCredit':h3cFcFLoginTxBbCredit,'h3cFcFLoginClass2RxMTU':h3cFcFLoginClass2RxMTU,'h3cFcFLoginClass3RxMTU':h3cFcFLoginClass3RxMTU,'h3cFcFLoginSuppClassRequested':h3cFcFLoginSuppClassRequested,'h3cFcFLoginClass2ReqAgreed':h3cFcFLoginClass2ReqAgreed,'h3cFcFLoginClass3ReqAgreed':h3cFcFLoginClass3ReqAgreed})