_H='hpnicfFcFLoginIndex'
_G='HPN-ICF-FC-FLOGIN-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='hpnicfVsanIndex'
_C='HPN-ICF-VSAN-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
HpnicfFcAddressId,HpnicfFcBbCredit,HpnicfFcClassOfServices,HpnicfFcNameId,HpnicfFcRxMTU=mibBuilder.importSymbols('HPN-ICF-FC-TC-MIB','HpnicfFcAddressId','HpnicfFcBbCredit','HpnicfFcClassOfServices','HpnicfFcNameId','HpnicfFcRxMTU')
hpnicfSan,hpnicfVsanIndex=mibBuilder.importSymbols(_C,'hpnicfSan',_D)
ifIndex,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
hpnicfFcFLogin=ModuleIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,3))
if mibBuilder.loadTexts:hpnicfFcFLogin.setRevisions(('2013-02-27 11:00',))
_HpnicfFcFLoginMibObjects_ObjectIdentity=ObjectIdentity
hpnicfFcFLoginMibObjects=_HpnicfFcFLoginMibObjects_ObjectIdentity((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1))
_HpnicfFcFLoginTable_Object=MibTable
hpnicfFcFLoginTable=_HpnicfFcFLoginTable_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1))
if mibBuilder.loadTexts:hpnicfFcFLoginTable.setStatus(_A)
_HpnicfFcFLoginEntry_Object=MibTableRow
hpnicfFcFLoginEntry=_HpnicfFcFLoginEntry_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1))
hpnicfFcFLoginEntry.setIndexNames((0,_E,_F),(0,_C,_D),(0,_G,_H))
if mibBuilder.loadTexts:hpnicfFcFLoginEntry.setStatus(_A)
_HpnicfFcFLoginIndex_Type=HpnicfFcAddressId
_HpnicfFcFLoginIndex_Object=MibTableColumn
hpnicfFcFLoginIndex=_HpnicfFcFLoginIndex_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,1),_HpnicfFcFLoginIndex_Type())
hpnicfFcFLoginIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hpnicfFcFLoginIndex.setStatus(_A)
_HpnicfFcFLoginPortNodeWWN_Type=HpnicfFcNameId
_HpnicfFcFLoginPortNodeWWN_Object=MibTableColumn
hpnicfFcFLoginPortNodeWWN=_HpnicfFcFLoginPortNodeWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,2),_HpnicfFcFLoginPortNodeWWN_Type())
hpnicfFcFLoginPortNodeWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginPortNodeWWN.setStatus(_A)
_HpnicfFcFLoginPortWWN_Type=HpnicfFcNameId
_HpnicfFcFLoginPortWWN_Object=MibTableColumn
hpnicfFcFLoginPortWWN=_HpnicfFcFLoginPortWWN_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,3),_HpnicfFcFLoginPortWWN_Type())
hpnicfFcFLoginPortWWN.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginPortWWN.setStatus(_A)
_HpnicfFcFLoginPortFcId_Type=HpnicfFcAddressId
_HpnicfFcFLoginPortFcId_Object=MibTableColumn
hpnicfFcFLoginPortFcId=_HpnicfFcFLoginPortFcId_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,4),_HpnicfFcFLoginPortFcId_Type())
hpnicfFcFLoginPortFcId.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginPortFcId.setStatus(_A)
_HpnicfFcFLoginRxBbCredit_Type=HpnicfFcBbCredit
_HpnicfFcFLoginRxBbCredit_Object=MibTableColumn
hpnicfFcFLoginRxBbCredit=_HpnicfFcFLoginRxBbCredit_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,5),_HpnicfFcFLoginRxBbCredit_Type())
hpnicfFcFLoginRxBbCredit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginRxBbCredit.setStatus(_A)
_HpnicfFcFLoginTxBbCredit_Type=HpnicfFcBbCredit
_HpnicfFcFLoginTxBbCredit_Object=MibTableColumn
hpnicfFcFLoginTxBbCredit=_HpnicfFcFLoginTxBbCredit_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,6),_HpnicfFcFLoginTxBbCredit_Type())
hpnicfFcFLoginTxBbCredit.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginTxBbCredit.setStatus(_A)
_HpnicfFcFLoginClass2RxMTU_Type=HpnicfFcRxMTU
_HpnicfFcFLoginClass2RxMTU_Object=MibTableColumn
hpnicfFcFLoginClass2RxMTU=_HpnicfFcFLoginClass2RxMTU_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,7),_HpnicfFcFLoginClass2RxMTU_Type())
hpnicfFcFLoginClass2RxMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginClass2RxMTU.setStatus(_A)
_HpnicfFcFLoginClass3RxMTU_Type=HpnicfFcRxMTU
_HpnicfFcFLoginClass3RxMTU_Object=MibTableColumn
hpnicfFcFLoginClass3RxMTU=_HpnicfFcFLoginClass3RxMTU_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,8),_HpnicfFcFLoginClass3RxMTU_Type())
hpnicfFcFLoginClass3RxMTU.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginClass3RxMTU.setStatus(_A)
_HpnicfFcFLoginSuppClassRequested_Type=HpnicfFcClassOfServices
_HpnicfFcFLoginSuppClassRequested_Object=MibTableColumn
hpnicfFcFLoginSuppClassRequested=_HpnicfFcFLoginSuppClassRequested_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,9),_HpnicfFcFLoginSuppClassRequested_Type())
hpnicfFcFLoginSuppClassRequested.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginSuppClassRequested.setStatus(_A)
_HpnicfFcFLoginClass2ReqAgreed_Type=TruthValue
_HpnicfFcFLoginClass2ReqAgreed_Object=MibTableColumn
hpnicfFcFLoginClass2ReqAgreed=_HpnicfFcFLoginClass2ReqAgreed_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,10),_HpnicfFcFLoginClass2ReqAgreed_Type())
hpnicfFcFLoginClass2ReqAgreed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginClass2ReqAgreed.setStatus(_A)
_HpnicfFcFLoginClass3ReqAgreed_Type=TruthValue
_HpnicfFcFLoginClass3ReqAgreed_Object=MibTableColumn
hpnicfFcFLoginClass3ReqAgreed=_HpnicfFcFLoginClass3ReqAgreed_Object((1,3,6,1,4,1,11,2,14,11,15,2,127,3,1,1,1,11),_HpnicfFcFLoginClass3ReqAgreed_Type())
hpnicfFcFLoginClass3ReqAgreed.setMaxAccess(_B)
if mibBuilder.loadTexts:hpnicfFcFLoginClass3ReqAgreed.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'hpnicfFcFLogin':hpnicfFcFLogin,'hpnicfFcFLoginMibObjects':hpnicfFcFLoginMibObjects,'hpnicfFcFLoginTable':hpnicfFcFLoginTable,'hpnicfFcFLoginEntry':hpnicfFcFLoginEntry,_H:hpnicfFcFLoginIndex,'hpnicfFcFLoginPortNodeWWN':hpnicfFcFLoginPortNodeWWN,'hpnicfFcFLoginPortWWN':hpnicfFcFLoginPortWWN,'hpnicfFcFLoginPortFcId':hpnicfFcFLoginPortFcId,'hpnicfFcFLoginRxBbCredit':hpnicfFcFLoginRxBbCredit,'hpnicfFcFLoginTxBbCredit':hpnicfFcFLoginTxBbCredit,'hpnicfFcFLoginClass2RxMTU':hpnicfFcFLoginClass2RxMTU,'hpnicfFcFLoginClass3RxMTU':hpnicfFcFLoginClass3RxMTU,'hpnicfFcFLoginSuppClassRequested':hpnicfFcFLoginSuppClassRequested,'hpnicfFcFLoginClass2ReqAgreed':hpnicfFcFLoginClass2ReqAgreed,'hpnicfFcFLoginClass3ReqAgreed':hpnicfFcFLoginClass3ReqAgreed})