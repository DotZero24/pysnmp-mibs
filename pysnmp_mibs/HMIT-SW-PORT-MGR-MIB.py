_U='copper'
_T='disable'
_S='speed13000M'
_R='speed2500M'
_Q='speed25000M'
_P='speed100G'
_O='speed40000M'
_N='speed10000M'
_M='speed1000M'
_L='speed100M'
_K='speed10M'
_J='speedauto'
_I='duplexfull'
_H='duplexhalf'
_G='hmITPortId'
_F='HMIT-SW-PORT-MGR-MIB'
_E='DisplayString'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
hmITSwitchTech,=mibBuilder.importSymbols('HMIT-SMI','hmITSwitchTech')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_E,'MacAddress','PhysAddress','RowStatus','TextualConvention')
hmITSwPortMIB=ModuleIdentity((1,3,6,1,4,1,248,100,1,6,3,1))
if mibBuilder.loadTexts:hmITSwPortMIB.setRevisions(('2010-01-08 17:00',))
_HmITSwPortmgrMIB_ObjectIdentity=ObjectIdentity
hmITSwPortmgrMIB=_HmITSwPortmgrMIB_ObjectIdentity((1,3,6,1,4,1,248,100,1,6,3,1,13))
_HmITPortmgrTable_Object=MibTable
hmITPortmgrTable=_HmITPortmgrTable_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2))
if mibBuilder.loadTexts:hmITPortmgrTable.setStatus(_A)
_HmITPortmgrEntry_Object=MibTableRow
hmITPortmgrEntry=_HmITPortmgrEntry_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1))
hmITPortmgrEntry.setIndexNames((0,_F,_G))
if mibBuilder.loadTexts:hmITPortmgrEntry.setStatus(_A)
class _HmITPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_HmITPortId_Type.__name__=_B
_HmITPortId_Object=MibTableColumn
hmITPortId=_HmITPortId_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,1),_HmITPortId_Type())
hmITPortId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:hmITPortId.setStatus(_A)
class _HmITMgrLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('noshutdown',1),('shutdown',2)))
_HmITMgrLinkStatus_Type.__name__=_B
_HmITMgrLinkStatus_Object=MibTableColumn
hmITMgrLinkStatus=_HmITMgrLinkStatus_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,2),_HmITMgrLinkStatus_Type())
hmITMgrLinkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITMgrLinkStatus.setStatus(_A)
class _HmITDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_HmITDescription_Type.__name__=_E
_HmITDescription_Object=MibTableColumn
hmITDescription=_HmITDescription_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,3),_HmITDescription_Type())
hmITDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITDescription.setStatus(_A)
class _HmITMgrDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('duplexauto',1),(_H,2),(_I,3)))
_HmITMgrDuplex_Type.__name__=_B
_HmITMgrDuplex_Object=MibTableColumn
hmITMgrDuplex=_HmITMgrDuplex_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,4),_HmITMgrDuplex_Type())
hmITMgrDuplex.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITMgrDuplex.setStatus(_A)
class _HmITMgrSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,11,12)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,11),(_S,12)))
_HmITMgrSpeed_Type.__name__=_B
_HmITMgrSpeed_Object=MibTableColumn
hmITMgrSpeed=_HmITMgrSpeed_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,5),_HmITMgrSpeed_Type())
hmITMgrSpeed.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITMgrSpeed.setStatus(_A)
class _HmITFlowControl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enable',1),(_T,2)))
_HmITFlowControl_Type.__name__=_B
_HmITFlowControl_Object=MibTableColumn
hmITFlowControl=_HmITFlowControl_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,6),_HmITFlowControl_Type())
hmITFlowControl.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITFlowControl.setStatus(_A)
class _HmITMdix_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('auto',1),('normal',2),('cross',3)))
_HmITMdix_Type.__name__=_B
_HmITMdix_Object=MibTableColumn
hmITMdix=_HmITMdix_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,7),_HmITMdix_Type())
hmITMdix.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITMdix.setStatus(_A)
class _HmITMtu_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(64,12288))
_HmITMtu_Type.__name__=_B
_HmITMtu_Object=MibTableColumn
hmITMtu=_HmITMtu_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,8),_HmITMtu_Type())
hmITMtu.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITMtu.setStatus(_A)
class _HmITLinkDelay_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10))
_HmITLinkDelay_Type.__name__=_B
_HmITLinkDelay_Object=MibTableColumn
hmITLinkDelay=_HmITLinkDelay_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,9),_HmITLinkDelay_Type())
hmITLinkDelay.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITLinkDelay.setStatus(_A)
class _HmITLoopBack_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_T,1),('internal',2),('external',3)))
_HmITLoopBack_Type.__name__=_B
_HmITLoopBack_Object=MibTableColumn
hmITLoopBack=_HmITLoopBack_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,10),_HmITLoopBack_Type())
hmITLoopBack.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITLoopBack.setStatus(_A)
class _HmITActualLinkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('up',1),('down',2)))
_HmITActualLinkStatus_Type.__name__=_B
_HmITActualLinkStatus_Object=MibTableColumn
hmITActualLinkStatus=_HmITActualLinkStatus_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,11),_HmITActualLinkStatus_Type())
hmITActualLinkStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITActualLinkStatus.setStatus(_A)
class _HmITActualDuplex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('duplexunknown',1),(_H,2),(_I,3)))
_HmITActualDuplex_Type.__name__=_B
_HmITActualDuplex_Object=MibTableColumn
hmITActualDuplex=_HmITActualDuplex_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,12),_HmITActualDuplex_Type())
hmITActualDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITActualDuplex.setStatus(_A)
class _HmITActualSpeed_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,11,12)));namedValues=NamedValues(*((_J,1),(_K,2),(_L,3),(_M,4),(_N,5),(_O,6),(_P,7),(_Q,8),(_R,11),(_S,12)))
_HmITActualSpeed_Type.__name__=_B
_HmITActualSpeed_Object=MibTableColumn
hmITActualSpeed=_HmITActualSpeed_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,13),_HmITActualSpeed_Type())
hmITActualSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITActualSpeed.setStatus(_A)
class _HmITPhyType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_U,1),('fiber',2)))
_HmITPhyType_Type.__name__=_B
_HmITPhyType_Object=MibTableColumn
hmITPhyType=_HmITPhyType_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,14),_HmITPhyType_Type())
hmITPhyType.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITPhyType.setStatus(_A)
_HmITPhyMacAddress_Type=MacAddress
_HmITPhyMacAddress_Object=MibTableColumn
hmITPhyMacAddress=_HmITPhyMacAddress_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,15),_HmITPhyMacAddress_Type())
hmITPhyMacAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITPhyMacAddress.setStatus(_A)
_HmITPortMgrPortAbility_Type=Counter64
_HmITPortMgrPortAbility_Object=MibTableColumn
hmITPortMgrPortAbility=_HmITPortMgrPortAbility_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,16),_HmITPortMgrPortAbility_Type())
hmITPortMgrPortAbility.setMaxAccess(_D)
if mibBuilder.loadTexts:hmITPortMgrPortAbility.setStatus(_A)
class _HmITPortMgrPortType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('lan',1),('wan',2)))
_HmITPortMgrPortType_Type.__name__=_B
_HmITPortMgrPortType_Object=MibTableColumn
hmITPortMgrPortType=_HmITPortMgrPortType_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,17),_HmITPortMgrPortType_Type())
hmITPortMgrPortType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITPortMgrPortType.setStatus(_A)
class _HmITPortMgrJumbo_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,10))
_HmITPortMgrJumbo_Type.__name__=_B
_HmITPortMgrJumbo_Object=MibTableColumn
hmITPortMgrJumbo=_HmITPortMgrJumbo_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,18),_HmITPortMgrJumbo_Type())
hmITPortMgrJumbo.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITPortMgrJumbo.setStatus(_A)
class _HmITPortMgrMediumType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('auto',1),(_U,2),('fiber',3),('fiber2copper',4)))
_HmITPortMgrMediumType_Type.__name__=_B
_HmITPortMgrMediumType_Object=MibTableColumn
hmITPortMgrMediumType=_HmITPortMgrMediumType_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,19),_HmITPortMgrMediumType_Type())
hmITPortMgrMediumType.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITPortMgrMediumType.setStatus(_A)
class _HmITPeerDescription_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,240))
_HmITPeerDescription_Type.__name__=_E
_HmITPeerDescription_Object=MibTableColumn
hmITPeerDescription=_HmITPeerDescription_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,20),_HmITPeerDescription_Type())
hmITPeerDescription.setMaxAccess(_C)
if mibBuilder.loadTexts:hmITPeerDescription.setStatus(_A)
_HmITPortMgrRowStatus_Type=RowStatus
_HmITPortMgrRowStatus_Object=MibTableColumn
hmITPortMgrRowStatus=_HmITPortMgrRowStatus_Object((1,3,6,1,4,1,248,100,1,6,3,1,13,2,1,21),_HmITPortMgrRowStatus_Type())
hmITPortMgrRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:hmITPortMgrRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'hmITSwPortMIB':hmITSwPortMIB,'hmITSwPortmgrMIB':hmITSwPortmgrMIB,'hmITPortmgrTable':hmITPortmgrTable,'hmITPortmgrEntry':hmITPortmgrEntry,_G:hmITPortId,'hmITMgrLinkStatus':hmITMgrLinkStatus,'hmITDescription':hmITDescription,'hmITMgrDuplex':hmITMgrDuplex,'hmITMgrSpeed':hmITMgrSpeed,'hmITFlowControl':hmITFlowControl,'hmITMdix':hmITMdix,'hmITMtu':hmITMtu,'hmITLinkDelay':hmITLinkDelay,'hmITLoopBack':hmITLoopBack,'hmITActualLinkStatus':hmITActualLinkStatus,'hmITActualDuplex':hmITActualDuplex,'hmITActualSpeed':hmITActualSpeed,'hmITPhyType':hmITPhyType,'hmITPhyMacAddress':hmITPhyMacAddress,'hmITPortMgrPortAbility':hmITPortMgrPortAbility,'hmITPortMgrPortType':hmITPortMgrPortType,'hmITPortMgrJumbo':hmITPortMgrJumbo,'hmITPortMgrMediumType':hmITPortMgrMediumType,'hmITPeerDescription':hmITPeerDescription,'hmITPortMgrRowStatus':hmITPortMgrRowStatus})