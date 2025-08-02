_D='bIPPortIndex'
_C='BENU-IP-MIB'
_B='read-only'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
benuPlatform,=mibBuilder.importSymbols('BENU-PLATFORM-MIB','benuPlatform')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
bIPMIB=ModuleIdentity((1,3,6,1,4,1,39406,1,6))
if mibBuilder.loadTexts:bIPMIB.setRevisions(('2014-12-17 00:00','2013-11-28 00:00','2013-05-31 00:00'))
_BIPNotifObjects_ObjectIdentity=ObjectIdentity
bIPNotifObjects=_BIPNotifObjects_ObjectIdentity((1,3,6,1,4,1,39406,1,6,0))
if mibBuilder.loadTexts:bIPNotifObjects.setStatus(_A)
_BIPMIBObjects_ObjectIdentity=ObjectIdentity
bIPMIBObjects=_BIPMIBObjects_ObjectIdentity((1,3,6,1,4,1,39406,1,6,1))
if mibBuilder.loadTexts:bIPMIBObjects.setStatus(_A)
_BIPPortTable_Object=MibTable
bIPPortTable=_BIPPortTable_Object((1,3,6,1,4,1,39406,1,6,1,1))
if mibBuilder.loadTexts:bIPPortTable.setStatus(_A)
_BIPPortEntry_Object=MibTableRow
bIPPortEntry=_BIPPortEntry_Object((1,3,6,1,4,1,39406,1,6,1,1,1))
bIPPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:bIPPortEntry.setStatus(_A)
_BIPPortIndex_Type=Unsigned32
_BIPPortIndex_Object=MibTableColumn
bIPPortIndex=_BIPPortIndex_Object((1,3,6,1,4,1,39406,1,6,1,1,1,1),_BIPPortIndex_Type())
bIPPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:bIPPortIndex.setStatus(_A)
_BIPPortInterfaceName_Type=DisplayString
_BIPPortInterfaceName_Object=MibTableColumn
bIPPortInterfaceName=_BIPPortInterfaceName_Object((1,3,6,1,4,1,39406,1,6,1,1,1,2),_BIPPortInterfaceName_Type())
bIPPortInterfaceName.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortInterfaceName.setStatus(_A)
_BIPPortTxBytesInFrameWoErr_Type=Counter64
_BIPPortTxBytesInFrameWoErr_Object=MibTableColumn
bIPPortTxBytesInFrameWoErr=_BIPPortTxBytesInFrameWoErr_Object((1,3,6,1,4,1,39406,1,6,1,1,1,3),_BIPPortTxBytesInFrameWoErr_Type())
bIPPortTxBytesInFrameWoErr.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTxBytesInFrameWoErr.setStatus(_A)
_BIPPortTxFramesWoErrExclPausFrame_Type=Counter64
_BIPPortTxFramesWoErrExclPausFrame_Object=MibTableColumn
bIPPortTxFramesWoErrExclPausFrame=_BIPPortTxFramesWoErrExclPausFrame_Object((1,3,6,1,4,1,39406,1,6,1,1,1,4),_BIPPortTxFramesWoErrExclPausFrame_Type())
bIPPortTxFramesWoErrExclPausFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTxFramesWoErrExclPausFrame.setStatus('deprecated')
_BIPPortTxBcastFrames_Type=Counter64
_BIPPortTxBcastFrames_Object=MibTableColumn
bIPPortTxBcastFrames=_BIPPortTxBcastFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,5),_BIPPortTxBcastFrames_Type())
bIPPortTxBcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTxBcastFrames.setStatus(_A)
_BIPPortTxL2McastFrames_Type=Counter64
_BIPPortTxL2McastFrames_Object=MibTableColumn
bIPPortTxL2McastFrames=_BIPPortTxL2McastFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,6),_BIPPortTxL2McastFrames_Type())
bIPPortTxL2McastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTxL2McastFrames.setStatus(_A)
_BIPPortTxPausFrame_Type=Counter64
_BIPPortTxPausFrame_Object=MibTableColumn
bIPPortTxPausFrame=_BIPPortTxPausFrame_Object((1,3,6,1,4,1,39406,1,6,1,1,1,7),_BIPPortTxPausFrame_Type())
bIPPortTxPausFrame.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTxPausFrame.setStatus(_A)
_BIPPortTx64byteFrames_Type=Counter64
_BIPPortTx64byteFrames_Object=MibTableColumn
bIPPortTx64byteFrames=_BIPPortTx64byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,8),_BIPPortTx64byteFrames_Type())
bIPPortTx64byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx64byteFrames.setStatus(_A)
_BIPPortTx65to127byteFrames_Type=Counter64
_BIPPortTx65to127byteFrames_Object=MibTableColumn
bIPPortTx65to127byteFrames=_BIPPortTx65to127byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,9),_BIPPortTx65to127byteFrames_Type())
bIPPortTx65to127byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx65to127byteFrames.setStatus(_A)
_BIPPortTx128to255byteFrames_Type=Counter64
_BIPPortTx128to255byteFrames_Object=MibTableColumn
bIPPortTx128to255byteFrames=_BIPPortTx128to255byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,10),_BIPPortTx128to255byteFrames_Type())
bIPPortTx128to255byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx128to255byteFrames.setStatus(_A)
_BIPPortTx256to511byteFrames_Type=Counter64
_BIPPortTx256to511byteFrames_Object=MibTableColumn
bIPPortTx256to511byteFrames=_BIPPortTx256to511byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,11),_BIPPortTx256to511byteFrames_Type())
bIPPortTx256to511byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx256to511byteFrames.setStatus(_A)
_BIPPortTx512to1023byteFrames_Type=Counter64
_BIPPortTx512to1023byteFrames_Object=MibTableColumn
bIPPortTx512to1023byteFrames=_BIPPortTx512to1023byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,12),_BIPPortTx512to1023byteFrames_Type())
bIPPortTx512to1023byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx512to1023byteFrames.setStatus(_A)
_BIPPortTx1024to1518byteFrames_Type=Counter64
_BIPPortTx1024to1518byteFrames_Object=MibTableColumn
bIPPortTx1024to1518byteFrames=_BIPPortTx1024to1518byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,13),_BIPPortTx1024to1518byteFrames_Type())
bIPPortTx1024to1518byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx1024to1518byteFrames.setStatus(_A)
_BIPPortTx1519to1522byteFrames_Type=Counter64
_BIPPortTx1519to1522byteFrames_Object=MibTableColumn
bIPPortTx1519to1522byteFrames=_BIPPortTx1519to1522byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,14),_BIPPortTx1519to1522byteFrames_Type())
bIPPortTx1519to1522byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx1519to1522byteFrames.setStatus(_A)
_BIPPortTx1523toMaxByteFrames_Type=Counter64
_BIPPortTx1523toMaxByteFrames_Object=MibTableColumn
bIPPortTx1523toMaxByteFrames=_BIPPortTx1523toMaxByteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,15),_BIPPortTx1523toMaxByteFrames_Type())
bIPPortTx1523toMaxByteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx1523toMaxByteFrames.setStatus(_A)
_BIPPortTx17to63byteFrames_Type=Counter64
_BIPPortTx17to63byteFrames_Object=MibTableColumn
bIPPortTx17to63byteFrames=_BIPPortTx17to63byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,16),_BIPPortTx17to63byteFrames_Type())
bIPPortTx17to63byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTx17to63byteFrames.setStatus(_A)
_BIPPortTxBadFcsFrames_Type=Counter64
_BIPPortTxBadFcsFrames_Object=MibTableColumn
bIPPortTxBadFcsFrames=_BIPPortTxBadFcsFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,17),_BIPPortTxBadFcsFrames_Type())
bIPPortTxBadFcsFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortTxBadFcsFrames.setStatus(_A)
_BIPPortRxBytesInFrameWoErr_Type=Counter64
_BIPPortRxBytesInFrameWoErr_Object=MibTableColumn
bIPPortRxBytesInFrameWoErr=_BIPPortRxBytesInFrameWoErr_Object((1,3,6,1,4,1,39406,1,6,1,1,1,18),_BIPPortRxBytesInFrameWoErr_Type())
bIPPortRxBytesInFrameWoErr.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxBytesInFrameWoErr.setStatus(_A)
_BIPPortRxBcastFrames_Type=Counter64
_BIPPortRxBcastFrames_Object=MibTableColumn
bIPPortRxBcastFrames=_BIPPortRxBcastFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,19),_BIPPortRxBcastFrames_Type())
bIPPortRxBcastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxBcastFrames.setStatus(_A)
_BIPPortRxL2McastFrames_Type=Counter64
_BIPPortRxL2McastFrames_Object=MibTableColumn
bIPPortRxL2McastFrames=_BIPPortRxL2McastFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,20),_BIPPortRxL2McastFrames_Type())
bIPPortRxL2McastFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxL2McastFrames.setStatus(_A)
_BIPPortRxPausFrames_Type=Counter64
_BIPPortRxPausFrames_Object=MibTableColumn
bIPPortRxPausFrames=_BIPPortRxPausFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,21),_BIPPortRxPausFrames_Type())
bIPPortRxPausFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxPausFrames.setStatus(_A)
_BIPPortRx64byteFrames_Type=Counter64
_BIPPortRx64byteFrames_Object=MibTableColumn
bIPPortRx64byteFrames=_BIPPortRx64byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,22),_BIPPortRx64byteFrames_Type())
bIPPortRx64byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRx64byteFrames.setStatus(_A)
_BIPPortRx65to127byteFrames_Type=Counter64
_BIPPortRx65to127byteFrames_Object=MibTableColumn
bIPPortRx65to127byteFrames=_BIPPortRx65to127byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,23),_BIPPortRx65to127byteFrames_Type())
bIPPortRx65to127byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRx65to127byteFrames.setStatus(_A)
_BIPPortRx128to255byteFrames_Type=Counter64
_BIPPortRx128to255byteFrames_Object=MibTableColumn
bIPPortRx128to255byteFrames=_BIPPortRx128to255byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,24),_BIPPortRx128to255byteFrames_Type())
bIPPortRx128to255byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRx128to255byteFrames.setStatus(_A)
_BIPPortRx256to511byteFrames_Type=Counter64
_BIPPortRx256to511byteFrames_Object=MibTableColumn
bIPPortRx256to511byteFrames=_BIPPortRx256to511byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,25),_BIPPortRx256to511byteFrames_Type())
bIPPortRx256to511byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRx256to511byteFrames.setStatus(_A)
_BIPPortRx512to1023byteFrames_Type=Counter64
_BIPPortRx512to1023byteFrames_Object=MibTableColumn
bIPPortRx512to1023byteFrames=_BIPPortRx512to1023byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,26),_BIPPortRx512to1023byteFrames_Type())
bIPPortRx512to1023byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRx512to1023byteFrames.setStatus(_A)
_BIPPortRx1024to1518byteFrames_Type=Counter64
_BIPPortRx1024to1518byteFrames_Object=MibTableColumn
bIPPortRx1024to1518byteFrames=_BIPPortRx1024to1518byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,27),_BIPPortRx1024to1518byteFrames_Type())
bIPPortRx1024to1518byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRx1024to1518byteFrames.setStatus(_A)
_BIPPortRx1519to1522byteFrames_Type=Counter64
_BIPPortRx1519to1522byteFrames_Object=MibTableColumn
bIPPortRx1519to1522byteFrames=_BIPPortRx1519to1522byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,28),_BIPPortRx1519to1522byteFrames_Type())
bIPPortRx1519to1522byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRx1519to1522byteFrames.setStatus(_A)
_BIPPortRx1523to10368byteFrames_Type=Counter64
_BIPPortRx1523to10368byteFrames_Object=MibTableColumn
bIPPortRx1523to10368byteFrames=_BIPPortRx1523to10368byteFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,29),_BIPPortRx1523to10368byteFrames_Type())
bIPPortRx1523to10368byteFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRx1523to10368byteFrames.setStatus(_A)
_BIPPortRxShortFrames_Type=Counter64
_BIPPortRxShortFrames_Object=MibTableColumn
bIPPortRxShortFrames=_BIPPortRxShortFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,30),_BIPPortRxShortFrames_Type())
bIPPortRxShortFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxShortFrames.setStatus(_A)
_BIPPortRxJabberFrames_Type=Counter64
_BIPPortRxJabberFrames_Object=MibTableColumn
bIPPortRxJabberFrames=_BIPPortRxJabberFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,31),_BIPPortRxJabberFrames_Type())
bIPPortRxJabberFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxJabberFrames.setStatus(_A)
_BIPPortRxOvrSzFrames_Type=Counter64
_BIPPortRxOvrSzFrames_Object=MibTableColumn
bIPPortRxOvrSzFrames=_BIPPortRxOvrSzFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,32),_BIPPortRxOvrSzFrames_Type())
bIPPortRxOvrSzFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxOvrSzFrames.setStatus(_A)
_BIPPortRxLenFldErrFrames_Type=Counter64
_BIPPortRxLenFldErrFrames_Object=MibTableColumn
bIPPortRxLenFldErrFrames=_BIPPortRxLenFldErrFrames_Object((1,3,6,1,4,1,39406,1,6,1,1,1,33),_BIPPortRxLenFldErrFrames_Type())
bIPPortRxLenFldErrFrames.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxLenFldErrFrames.setStatus(_A)
_BIPPortRxSymbErrs_Type=Counter64
_BIPPortRxSymbErrs_Object=MibTableColumn
bIPPortRxSymbErrs=_BIPPortRxSymbErrs_Object((1,3,6,1,4,1,39406,1,6,1,1,1,34),_BIPPortRxSymbErrs_Type())
bIPPortRxSymbErrs.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxSymbErrs.setStatus(_A)
_BIPPortRxIntrPktJunk_Type=Counter64
_BIPPortRxIntrPktJunk_Object=MibTableColumn
bIPPortRxIntrPktJunk=_BIPPortRxIntrPktJunk_Object((1,3,6,1,4,1,39406,1,6,1,1,1,35),_BIPPortRxIntrPktJunk_Type())
bIPPortRxIntrPktJunk.setMaxAccess(_B)
if mibBuilder.loadTexts:bIPPortRxIntrPktJunk.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'bIPMIB':bIPMIB,'bIPNotifObjects':bIPNotifObjects,'bIPMIBObjects':bIPMIBObjects,'bIPPortTable':bIPPortTable,'bIPPortEntry':bIPPortEntry,_D:bIPPortIndex,'bIPPortInterfaceName':bIPPortInterfaceName,'bIPPortTxBytesInFrameWoErr':bIPPortTxBytesInFrameWoErr,'bIPPortTxFramesWoErrExclPausFrame':bIPPortTxFramesWoErrExclPausFrame,'bIPPortTxBcastFrames':bIPPortTxBcastFrames,'bIPPortTxL2McastFrames':bIPPortTxL2McastFrames,'bIPPortTxPausFrame':bIPPortTxPausFrame,'bIPPortTx64byteFrames':bIPPortTx64byteFrames,'bIPPortTx65to127byteFrames':bIPPortTx65to127byteFrames,'bIPPortTx128to255byteFrames':bIPPortTx128to255byteFrames,'bIPPortTx256to511byteFrames':bIPPortTx256to511byteFrames,'bIPPortTx512to1023byteFrames':bIPPortTx512to1023byteFrames,'bIPPortTx1024to1518byteFrames':bIPPortTx1024to1518byteFrames,'bIPPortTx1519to1522byteFrames':bIPPortTx1519to1522byteFrames,'bIPPortTx1523toMaxByteFrames':bIPPortTx1523toMaxByteFrames,'bIPPortTx17to63byteFrames':bIPPortTx17to63byteFrames,'bIPPortTxBadFcsFrames':bIPPortTxBadFcsFrames,'bIPPortRxBytesInFrameWoErr':bIPPortRxBytesInFrameWoErr,'bIPPortRxBcastFrames':bIPPortRxBcastFrames,'bIPPortRxL2McastFrames':bIPPortRxL2McastFrames,'bIPPortRxPausFrames':bIPPortRxPausFrames,'bIPPortRx64byteFrames':bIPPortRx64byteFrames,'bIPPortRx65to127byteFrames':bIPPortRx65to127byteFrames,'bIPPortRx128to255byteFrames':bIPPortRx128to255byteFrames,'bIPPortRx256to511byteFrames':bIPPortRx256to511byteFrames,'bIPPortRx512to1023byteFrames':bIPPortRx512to1023byteFrames,'bIPPortRx1024to1518byteFrames':bIPPortRx1024to1518byteFrames,'bIPPortRx1519to1522byteFrames':bIPPortRx1519to1522byteFrames,'bIPPortRx1523to10368byteFrames':bIPPortRx1523to10368byteFrames,'bIPPortRxShortFrames':bIPPortRxShortFrames,'bIPPortRxJabberFrames':bIPPortRxJabberFrames,'bIPPortRxOvrSzFrames':bIPPortRxOvrSzFrames,'bIPPortRxLenFldErrFrames':bIPPortRxLenFldErrFrames,'bIPPortRxSymbErrs':bIPPortRxSymbErrs,'bIPPortRxIntrPktJunk':bIPPortRxIntrPktJunk})