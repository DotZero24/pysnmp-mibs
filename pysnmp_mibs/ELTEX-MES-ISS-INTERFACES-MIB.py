_L='eltMesIssPortCtrlEntry'
_K='not-accessible'
_J='eltMesIssHardwareSerdesRxConfigLaneNumber'
_I='eltMesIssHardwareSerdesRxConfigIfIndex'
_H='copper'
_G='TruthValue'
_F='unknown'
_E='ELTEX-MES-ISS-INTERFACES-MIB'
_D='read-only'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
issPortCtrlEntry,=mibBuilder.importSymbols('ARICENT-ISS-MIB','issPortCtrlEntry')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention',_G)
eltMesIssInterfacesMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,4))
if mibBuilder.loadTexts:eltMesIssInterfacesMIB.setRevisions(('2022-10-19 00:00','2021-03-29 00:00','2021-01-19 00:00','2018-12-19 00:00'))
class EltMesIssPortCtrlAutoNegBits(TextualConvention,Bits):status=_A;namedValues=NamedValues(*(('default',0),(_F,1),('half10M',2),('full10M',3),('half100M',4),('full100M',5),('full1G',7)))
_EltMesIssInterfacesObjects_ObjectIdentity=ObjectIdentity
eltMesIssInterfacesObjects=_EltMesIssInterfacesObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,4,1))
_EltMesIssInterfacesGlobals_ObjectIdentity=ObjectIdentity
eltMesIssInterfacesGlobals=_EltMesIssInterfacesGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,4,1,1))
_EltMesIssDefaultInterface_Type=Integer32
_EltMesIssDefaultInterface_Object=MibScalar
eltMesIssDefaultInterface=_EltMesIssDefaultInterface_Object((1,3,6,1,4,1,35265,1,139,4,1,1,1),_EltMesIssDefaultInterface_Type())
eltMesIssDefaultInterface.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssDefaultInterface.setStatus(_A)
_EltMesIssInterfacesConfig_ObjectIdentity=ObjectIdentity
eltMesIssInterfacesConfig=_EltMesIssInterfacesConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,4,1,2))
_EltMesIssPortCtrlTable_Object=MibTable
eltMesIssPortCtrlTable=_EltMesIssPortCtrlTable_Object((1,3,6,1,4,1,35265,1,139,4,1,2,1))
if mibBuilder.loadTexts:eltMesIssPortCtrlTable.setStatus(_A)
_EltMesIssPortCtrlEntry_Object=MibTableRow
eltMesIssPortCtrlEntry=_EltMesIssPortCtrlEntry_Object((1,3,6,1,4,1,35265,1,139,4,1,2,1,1))
if mibBuilder.loadTexts:eltMesIssPortCtrlEntry.setStatus(_A)
class _EltMesIssPortCtrlAdminComboMode_Type(Integer32):defaultValue=3;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('force-fiber',1),('force-copper',2),('prefer-fiber',3),('prefer-copper',4)))
_EltMesIssPortCtrlAdminComboMode_Type.__name__=_B
_EltMesIssPortCtrlAdminComboMode_Object=MibTableColumn
eltMesIssPortCtrlAdminComboMode=_EltMesIssPortCtrlAdminComboMode_Object((1,3,6,1,4,1,35265,1,139,4,1,2,1,1,1),_EltMesIssPortCtrlAdminComboMode_Type())
eltMesIssPortCtrlAdminComboMode.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssPortCtrlAdminComboMode.setStatus(_A)
class _EltMesIssPortCtrlOperComboMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('fiber',1),(_H,2),(_F,3)))
_EltMesIssPortCtrlOperComboMode_Type.__name__=_B
_EltMesIssPortCtrlOperComboMode_Object=MibTableColumn
eltMesIssPortCtrlOperComboMode=_EltMesIssPortCtrlOperComboMode_Object((1,3,6,1,4,1,35265,1,139,4,1,2,1,1,2),_EltMesIssPortCtrlOperComboMode_Type())
eltMesIssPortCtrlOperComboMode.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPortCtrlOperComboMode.setStatus(_A)
_EltMesIssPortCtrlAutoNegAdminLocal_Type=EltMesIssPortCtrlAutoNegBits
_EltMesIssPortCtrlAutoNegAdminLocal_Object=MibTableColumn
eltMesIssPortCtrlAutoNegAdminLocal=_EltMesIssPortCtrlAutoNegAdminLocal_Object((1,3,6,1,4,1,35265,1,139,4,1,2,1,1,3),_EltMesIssPortCtrlAutoNegAdminLocal_Type())
eltMesIssPortCtrlAutoNegAdminLocal.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssPortCtrlAutoNegAdminLocal.setStatus(_A)
_EltMesIssPortCtrlAutoNegOperLocal_Type=EltMesIssPortCtrlAutoNegBits
_EltMesIssPortCtrlAutoNegOperLocal_Object=MibTableColumn
eltMesIssPortCtrlAutoNegOperLocal=_EltMesIssPortCtrlAutoNegOperLocal_Object((1,3,6,1,4,1,35265,1,139,4,1,2,1,1,4),_EltMesIssPortCtrlAutoNegOperLocal_Type())
eltMesIssPortCtrlAutoNegOperLocal.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPortCtrlAutoNegOperLocal.setStatus(_A)
class _EltMesIssPortCtrlTransceiverType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_H,1),('fiberOptics',2),('combo',3)))
_EltMesIssPortCtrlTransceiverType_Type.__name__=_B
_EltMesIssPortCtrlTransceiverType_Object=MibTableColumn
eltMesIssPortCtrlTransceiverType=_EltMesIssPortCtrlTransceiverType_Object((1,3,6,1,4,1,35265,1,139,4,1,2,1,1,5),_EltMesIssPortCtrlTransceiverType_Type())
eltMesIssPortCtrlTransceiverType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPortCtrlTransceiverType.setStatus(_A)
class _EltMesIssPortCtrlType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7,8,9,10)));namedValues=NamedValues(*(('eth10M',1),('eth100M',2),('eth1000M',3),('eth2500M',4),('eth5G',5),('eth10G',6),('eth20G',7),('eth40G',8),('eth100G',9),(_F,10)))
_EltMesIssPortCtrlType_Type.__name__=_B
_EltMesIssPortCtrlType_Object=MibTableColumn
eltMesIssPortCtrlType=_EltMesIssPortCtrlType_Object((1,3,6,1,4,1,35265,1,139,4,1,2,1,1,6),_EltMesIssPortCtrlType_Type())
eltMesIssPortCtrlType.setMaxAccess(_D)
if mibBuilder.loadTexts:eltMesIssPortCtrlType.setStatus(_A)
_EltMesIssHardwareSerdesRxConfigTable_Object=MibTable
eltMesIssHardwareSerdesRxConfigTable=_EltMesIssHardwareSerdesRxConfigTable_Object((1,3,6,1,4,1,35265,1,139,4,1,2,2))
if mibBuilder.loadTexts:eltMesIssHardwareSerdesRxConfigTable.setStatus(_A)
_EltMesIssHardwareSerdesRxConfigEntry_Object=MibTableRow
eltMesIssHardwareSerdesRxConfigEntry=_EltMesIssHardwareSerdesRxConfigEntry_Object((1,3,6,1,4,1,35265,1,139,4,1,2,2,1))
eltMesIssHardwareSerdesRxConfigEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:eltMesIssHardwareSerdesRxConfigEntry.setStatus(_A)
_EltMesIssHardwareSerdesRxConfigIfIndex_Type=Integer32
_EltMesIssHardwareSerdesRxConfigIfIndex_Object=MibTableColumn
eltMesIssHardwareSerdesRxConfigIfIndex=_EltMesIssHardwareSerdesRxConfigIfIndex_Object((1,3,6,1,4,1,35265,1,139,4,1,2,2,1,1),_EltMesIssHardwareSerdesRxConfigIfIndex_Type())
eltMesIssHardwareSerdesRxConfigIfIndex.setMaxAccess(_K)
if mibBuilder.loadTexts:eltMesIssHardwareSerdesRxConfigIfIndex.setStatus(_A)
_EltMesIssHardwareSerdesRxConfigLaneNumber_Type=Integer32
_EltMesIssHardwareSerdesRxConfigLaneNumber_Object=MibTableColumn
eltMesIssHardwareSerdesRxConfigLaneNumber=_EltMesIssHardwareSerdesRxConfigLaneNumber_Object((1,3,6,1,4,1,35265,1,139,4,1,2,2,1,2),_EltMesIssHardwareSerdesRxConfigLaneNumber_Type())
eltMesIssHardwareSerdesRxConfigLaneNumber.setMaxAccess(_K)
if mibBuilder.loadTexts:eltMesIssHardwareSerdesRxConfigLaneNumber.setStatus(_A)
class _EltMesIssHardwareSerdesRxConfigUserParamsEnable_Type(TruthValue):defaultValue=2
_EltMesIssHardwareSerdesRxConfigUserParamsEnable_Type.__name__=_G
_EltMesIssHardwareSerdesRxConfigUserParamsEnable_Object=MibTableColumn
eltMesIssHardwareSerdesRxConfigUserParamsEnable=_EltMesIssHardwareSerdesRxConfigUserParamsEnable_Object((1,3,6,1,4,1,35265,1,139,4,1,2,2,1,3),_EltMesIssHardwareSerdesRxConfigUserParamsEnable_Type())
eltMesIssHardwareSerdesRxConfigUserParamsEnable.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssHardwareSerdesRxConfigUserParamsEnable.setStatus(_A)
class _EltMesIssHardwareSerdesRxConfigLeq_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,31))
_EltMesIssHardwareSerdesRxConfigLeq_Type.__name__=_B
_EltMesIssHardwareSerdesRxConfigLeq_Object=MibTableColumn
eltMesIssHardwareSerdesRxConfigLeq=_EltMesIssHardwareSerdesRxConfigLeq_Object((1,3,6,1,4,1,35265,1,139,4,1,2,2,1,4),_EltMesIssHardwareSerdesRxConfigLeq_Type())
eltMesIssHardwareSerdesRxConfigLeq.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssHardwareSerdesRxConfigLeq.setStatus(_A)
issPortCtrlEntry.registerAugmentions((_E,_L))
eltMesIssPortCtrlEntry.setIndexNames(*issPortCtrlEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'EltMesIssPortCtrlAutoNegBits':EltMesIssPortCtrlAutoNegBits,'eltMesIssInterfacesMIB':eltMesIssInterfacesMIB,'eltMesIssInterfacesObjects':eltMesIssInterfacesObjects,'eltMesIssInterfacesGlobals':eltMesIssInterfacesGlobals,'eltMesIssDefaultInterface':eltMesIssDefaultInterface,'eltMesIssInterfacesConfig':eltMesIssInterfacesConfig,'eltMesIssPortCtrlTable':eltMesIssPortCtrlTable,_L:eltMesIssPortCtrlEntry,'eltMesIssPortCtrlAdminComboMode':eltMesIssPortCtrlAdminComboMode,'eltMesIssPortCtrlOperComboMode':eltMesIssPortCtrlOperComboMode,'eltMesIssPortCtrlAutoNegAdminLocal':eltMesIssPortCtrlAutoNegAdminLocal,'eltMesIssPortCtrlAutoNegOperLocal':eltMesIssPortCtrlAutoNegOperLocal,'eltMesIssPortCtrlTransceiverType':eltMesIssPortCtrlTransceiverType,'eltMesIssPortCtrlType':eltMesIssPortCtrlType,'eltMesIssHardwareSerdesRxConfigTable':eltMesIssHardwareSerdesRxConfigTable,'eltMesIssHardwareSerdesRxConfigEntry':eltMesIssHardwareSerdesRxConfigEntry,_I:eltMesIssHardwareSerdesRxConfigIfIndex,_J:eltMesIssHardwareSerdesRxConfigLaneNumber,'eltMesIssHardwareSerdesRxConfigUserParamsEnable':eltMesIssHardwareSerdesRxConfigUserParamsEnable,'eltMesIssHardwareSerdesRxConfigLeq':eltMesIssHardwareSerdesRxConfigLeq})