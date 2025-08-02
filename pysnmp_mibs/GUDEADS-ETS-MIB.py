_R='etsPowerSelectEvt'
_Q='etsManualSelectEvt'
_P='etsSecondaryPowerChangeEvt'
_O='etsPrimaryPowerChangeEvt'
_N='etsTrapIPPort'
_M='etsTrapIPAddr'
_L='etsTrapCtrl'
_K='etsTrapIPIndex'
_J='IpAddress'
_I='etsPowerSelect'
_H='etsSecManualSelect'
_G='etsSecPowAvail'
_F='etsPrimPowAvail'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='current'
_A='GUDEADS-ETS-MIB'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,_J,'ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
gudeads=ModuleIdentity((1,3,6,1,4,1,28507))
if mibBuilder.loadTexts:gudeads.setRevisions(('2007-05-23 12:44',))
_GadsETS_ObjectIdentity=ObjectIdentity
gadsETS=_GadsETS_ObjectIdentity((1,3,6,1,4,1,28507,4))
_EtsEvents_ObjectIdentity=ObjectIdentity
etsEvents=_EtsEvents_ObjectIdentity((1,3,6,1,4,1,28507,4,0))
_EtsObjects_ObjectIdentity=ObjectIdentity
etsObjects=_EtsObjects_ObjectIdentity((1,3,6,1,4,1,28507,4,1))
_EtsSNMPaccess_ObjectIdentity=ObjectIdentity
etsSNMPaccess=_EtsSNMPaccess_ObjectIdentity((1,3,6,1,4,1,28507,4,1,1))
class _EtsTrapCtrl_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2))
_EtsTrapCtrl_Type.__name__=_C
_EtsTrapCtrl_Object=MibScalar
etsTrapCtrl=_EtsTrapCtrl_Object((1,3,6,1,4,1,28507,4,1,1,1),_EtsTrapCtrl_Type())
etsTrapCtrl.setMaxAccess(_E)
if mibBuilder.loadTexts:etsTrapCtrl.setStatus(_B)
_EtsTrapIPTable_Object=MibTable
etsTrapIPTable=_EtsTrapIPTable_Object((1,3,6,1,4,1,28507,4,1,1,2))
if mibBuilder.loadTexts:etsTrapIPTable.setStatus(_B)
_EtsTrapIPEntry_Object=MibTableRow
etsTrapIPEntry=_EtsTrapIPEntry_Object((1,3,6,1,4,1,28507,4,1,1,2,1))
etsTrapIPEntry.setIndexNames((0,_A,_K))
if mibBuilder.loadTexts:etsTrapIPEntry.setStatus(_B)
class _EtsTrapIPIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,8))
_EtsTrapIPIndex_Type.__name__=_C
_EtsTrapIPIndex_Object=MibTableColumn
etsTrapIPIndex=_EtsTrapIPIndex_Object((1,3,6,1,4,1,28507,4,1,1,2,1,1),_EtsTrapIPIndex_Type())
etsTrapIPIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:etsTrapIPIndex.setStatus(_B)
class _EtsTrapIPAddr_Type(IpAddress):defaultHexValue='00000000'
_EtsTrapIPAddr_Type.__name__=_J
_EtsTrapIPAddr_Object=MibTableColumn
etsTrapIPAddr=_EtsTrapIPAddr_Object((1,3,6,1,4,1,28507,4,1,1,2,1,2),_EtsTrapIPAddr_Type())
etsTrapIPAddr.setMaxAccess(_E)
if mibBuilder.loadTexts:etsTrapIPAddr.setStatus(_B)
class _EtsTrapIPPort_Type(Integer32):defaultValue=162;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1024))
_EtsTrapIPPort_Type.__name__=_C
_EtsTrapIPPort_Object=MibTableColumn
etsTrapIPPort=_EtsTrapIPPort_Object((1,3,6,1,4,1,28507,4,1,1,2,1,3),_EtsTrapIPPort_Type())
etsTrapIPPort.setMaxAccess(_E)
if mibBuilder.loadTexts:etsTrapIPPort.setStatus(_B)
_EtsPrimPowAvail_Type=Integer32
_EtsPrimPowAvail_Object=MibScalar
etsPrimPowAvail=_EtsPrimPowAvail_Object((1,3,6,1,4,1,28507,4,1,2),_EtsPrimPowAvail_Type())
etsPrimPowAvail.setMaxAccess(_D)
if mibBuilder.loadTexts:etsPrimPowAvail.setStatus(_B)
_EtsSecPowAvail_Type=Integer32
_EtsSecPowAvail_Object=MibScalar
etsSecPowAvail=_EtsSecPowAvail_Object((1,3,6,1,4,1,28507,4,1,3),_EtsSecPowAvail_Type())
etsSecPowAvail.setMaxAccess(_D)
if mibBuilder.loadTexts:etsSecPowAvail.setStatus(_B)
_EtsSecManualSelect_Type=Integer32
_EtsSecManualSelect_Object=MibScalar
etsSecManualSelect=_EtsSecManualSelect_Object((1,3,6,1,4,1,28507,4,1,4),_EtsSecManualSelect_Type())
etsSecManualSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:etsSecManualSelect.setStatus(_B)
_EtsPowerSelect_Type=Integer32
_EtsPowerSelect_Object=MibScalar
etsPowerSelect=_EtsPowerSelect_Object((1,3,6,1,4,1,28507,4,1,5),_EtsPowerSelect_Type())
etsPowerSelect.setMaxAccess(_D)
if mibBuilder.loadTexts:etsPowerSelect.setStatus(_B)
_EtsConf_ObjectIdentity=ObjectIdentity
etsConf=_EtsConf_ObjectIdentity((1,3,6,1,4,1,28507,4,3))
_EtsGroups_ObjectIdentity=ObjectIdentity
etsGroups=_EtsGroups_ObjectIdentity((1,3,6,1,4,1,28507,4,3,1))
_EtsCompls_ObjectIdentity=ObjectIdentity
etsCompls=_EtsCompls_ObjectIdentity((1,3,6,1,4,1,28507,4,3,2))
etsBasicGroup=ObjectGroup((1,3,6,1,4,1,28507,4,3,1,1))
etsBasicGroup.setObjects(*((_A,_F),(_A,_G),(_A,_H),(_A,_I),(_A,_L),(_A,_M),(_A,_N)))
if mibBuilder.loadTexts:etsBasicGroup.setStatus(_B)
etsPrimaryPowerChangeEvt=NotificationType((1,3,6,1,4,1,28507,4,0,1))
etsPrimaryPowerChangeEvt.setObjects((_A,_F))
if mibBuilder.loadTexts:etsPrimaryPowerChangeEvt.setStatus(_B)
etsSecondaryPowerChangeEvt=NotificationType((1,3,6,1,4,1,28507,4,0,2))
etsSecondaryPowerChangeEvt.setObjects((_A,_G))
if mibBuilder.loadTexts:etsSecondaryPowerChangeEvt.setStatus(_B)
etsManualSelectEvt=NotificationType((1,3,6,1,4,1,28507,4,0,3))
etsManualSelectEvt.setObjects((_A,_H))
if mibBuilder.loadTexts:etsManualSelectEvt.setStatus(_B)
etsPowerSelectEvt=NotificationType((1,3,6,1,4,1,28507,4,0,4))
etsPowerSelectEvt.setObjects((_A,_I))
if mibBuilder.loadTexts:etsPowerSelectEvt.setStatus(_B)
etsNotificationGroup=NotificationGroup((1,3,6,1,4,1,28507,4,3,1,2))
etsNotificationGroup.setObjects(*((_A,_O),(_A,_P),(_A,_Q),(_A,_R)))
if mibBuilder.loadTexts:etsNotificationGroup.setStatus(_B)
mibBuilder.exportSymbols(_A,**{'gudeads':gudeads,'gadsETS':gadsETS,'etsEvents':etsEvents,_O:etsPrimaryPowerChangeEvt,_P:etsSecondaryPowerChangeEvt,_Q:etsManualSelectEvt,_R:etsPowerSelectEvt,'etsObjects':etsObjects,'etsSNMPaccess':etsSNMPaccess,_L:etsTrapCtrl,'etsTrapIPTable':etsTrapIPTable,'etsTrapIPEntry':etsTrapIPEntry,_K:etsTrapIPIndex,_M:etsTrapIPAddr,_N:etsTrapIPPort,_F:etsPrimPowAvail,_G:etsSecPowAvail,_H:etsSecManualSelect,_I:etsPowerSelect,'etsConf':etsConf,'etsGroups':etsGroups,'etsBasicGroup':etsBasicGroup,'etsNotificationGroup':etsNotificationGroup,'etsCompls':etsCompls})