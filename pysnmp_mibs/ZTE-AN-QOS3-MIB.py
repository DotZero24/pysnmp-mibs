_k='zxAnQosAtmTrafficPrfName'
_j='zxAnQosTrafficIfVlanDirection'
_i='lowPriorityFirst'
_h='noDistinction'
_g='zxAnQosTrafficPrfName'
_f='zxAnQosQueueMapPrfName'
_e='zxAnQosQueueBlockPrfName'
_d='servicePort'
_c='zxAnQosCosToMplsTcPrfName'
_b='zxAnQosMplsTcToCosPrfName'
_a='zxAnQosDscpToDropPrecedePrfName'
_Z='zxAnQosDscpToCosPrfName'
_Y='zxAnQosDscpToDscpPrfName'
_X='zxAnQosCosToCosPrfName'
_W='dscpToCos'
_V='cosRemark'
_U='override'
_T='trust'
_S='read-only'
_R='notSupport'
_Q='kbytes'
_P='zxAnQos3LogicalId'
_O='zxAnQos3VCircuitType'
_N='zxAnQos3Onu'
_M='zxAnQos3Port'
_L='zxAnQos3Slot'
_K='zxAnQos3Shelf'
_J='zxAnQos3Rack'
_I='kbps'
_H='OctetString'
_G='not-accessible'
_F='DisplayString'
_E='read-write'
_D='Integer32'
_C='read-create'
_B='ZTE-AN-QOS3-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_H,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention')
zxAn,=mibBuilder.importSymbols('ZTE-AN-TC-MIB','zxAn')
zxAnQosMib=ModuleIdentity((1,3,6,1,4,1,3902,1015,21))
_ZxAnQos3Objects_ObjectIdentity=ObjectIdentity
zxAnQos3Objects=_ZxAnQos3Objects_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,4))
_ZxAnQos3GlobalObjects_ObjectIdentity=ObjectIdentity
zxAnQos3GlobalObjects=_ZxAnQos3GlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,4,1))
class _ZxAnQos3MgmtCapabilities_Type(Bits):namedValues=NamedValues(*(('supportQos3',0),('supportTrafficPrfType',1),('supportPvc2Queue',2),('supportTrafficColorMode',3)))
_ZxAnQos3MgmtCapabilities_Type.__name__='Bits'
_ZxAnQos3MgmtCapabilities_Object=MibScalar
zxAnQos3MgmtCapabilities=_ZxAnQos3MgmtCapabilities_Object((1,3,6,1,4,1,3902,1015,21,4,1,1),_ZxAnQos3MgmtCapabilities_Type())
zxAnQos3MgmtCapabilities.setMaxAccess(_S)
if mibBuilder.loadTexts:zxAnQos3MgmtCapabilities.setStatus(_A)
_ZxAnQos3QueueGlobalObjects_ObjectIdentity=ObjectIdentity
zxAnQos3QueueGlobalObjects=_ZxAnQos3QueueGlobalObjects_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,4,1,2))
class _ZxAnQosEthCosToQueue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosEthCosToQueue_Type.__name__=_H
_ZxAnQosEthCosToQueue_Object=MibScalar
zxAnQosEthCosToQueue=_ZxAnQosEthCosToQueue_Object((1,3,6,1,4,1,3902,1015,21,4,1,2,1),_ZxAnQosEthCosToQueue_Type())
zxAnQosEthCosToQueue.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosEthCosToQueue.setStatus(_A)
_ZxAnQos3MappingProfile_ObjectIdentity=ObjectIdentity
zxAnQos3MappingProfile=_ZxAnQos3MappingProfile_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,4,2))
_ZxAnQos3CosRemarkProfileTable_Object=MibTable
zxAnQos3CosRemarkProfileTable=_ZxAnQos3CosRemarkProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,2,1))
if mibBuilder.loadTexts:zxAnQos3CosRemarkProfileTable.setStatus(_A)
_ZxAnQos3CosRemarkProfileEntry_Object=MibTableRow
zxAnQos3CosRemarkProfileEntry=_ZxAnQos3CosRemarkProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,2,1,1))
zxAnQos3CosRemarkProfileEntry.setIndexNames((0,_B,_X))
if mibBuilder.loadTexts:zxAnQos3CosRemarkProfileEntry.setStatus(_A)
class _ZxAnQosCosToCosPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosCosToCosPrfName_Type.__name__=_F
_ZxAnQosCosToCosPrfName_Object=MibTableColumn
zxAnQosCosToCosPrfName=_ZxAnQosCosToCosPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,2,1,1,1),_ZxAnQosCosToCosPrfName_Type())
zxAnQosCosToCosPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosCosToCosPrfName.setStatus(_A)
class _ZxAnQosCosToCos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosCosToCos_Type.__name__=_H
_ZxAnQosCosToCos_Object=MibTableColumn
zxAnQosCosToCos=_ZxAnQosCosToCos_Object((1,3,6,1,4,1,3902,1015,21,4,2,1,1,2),_ZxAnQosCosToCos_Type())
zxAnQosCosToCos.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosCosToCos.setStatus(_A)
_ZxAnQosCosToCosPrfRowStatus_Type=RowStatus
_ZxAnQosCosToCosPrfRowStatus_Object=MibTableColumn
zxAnQosCosToCosPrfRowStatus=_ZxAnQosCosToCosPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,2,1,1,20),_ZxAnQosCosToCosPrfRowStatus_Type())
zxAnQosCosToCosPrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosCosToCosPrfRowStatus.setStatus(_A)
_ZxAnQos3DscpRemarkProfileTable_Object=MibTable
zxAnQos3DscpRemarkProfileTable=_ZxAnQos3DscpRemarkProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,2,2))
if mibBuilder.loadTexts:zxAnQos3DscpRemarkProfileTable.setStatus(_A)
_ZxAnQos3DscpRemarkProfileEntry_Object=MibTableRow
zxAnQos3DscpRemarkProfileEntry=_ZxAnQos3DscpRemarkProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,2,2,1))
zxAnQos3DscpRemarkProfileEntry.setIndexNames((0,_B,_Y))
if mibBuilder.loadTexts:zxAnQos3DscpRemarkProfileEntry.setStatus(_A)
class _ZxAnQosDscpToDscpPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosDscpToDscpPrfName_Type.__name__=_F
_ZxAnQosDscpToDscpPrfName_Object=MibTableColumn
zxAnQosDscpToDscpPrfName=_ZxAnQosDscpToDscpPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,2,2,1,1),_ZxAnQosDscpToDscpPrfName_Type())
zxAnQosDscpToDscpPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosDscpToDscpPrfName.setStatus(_A)
class _ZxAnQosDscpToDscp_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ZxAnQosDscpToDscp_Type.__name__=_H
_ZxAnQosDscpToDscp_Object=MibTableColumn
zxAnQosDscpToDscp=_ZxAnQosDscpToDscp_Object((1,3,6,1,4,1,3902,1015,21,4,2,2,1,2),_ZxAnQosDscpToDscp_Type())
zxAnQosDscpToDscp.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosDscpToDscp.setStatus(_A)
_ZxAnQosDscpToDscpPrfRowStatus_Type=RowStatus
_ZxAnQosDscpToDscpPrfRowStatus_Object=MibTableColumn
zxAnQosDscpToDscpPrfRowStatus=_ZxAnQosDscpToDscpPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,2,2,1,20),_ZxAnQosDscpToDscpPrfRowStatus_Type())
zxAnQosDscpToDscpPrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosDscpToDscpPrfRowStatus.setStatus(_A)
_ZxAnQos3Dscp2CosProfileTable_Object=MibTable
zxAnQos3Dscp2CosProfileTable=_ZxAnQos3Dscp2CosProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,2,3))
if mibBuilder.loadTexts:zxAnQos3Dscp2CosProfileTable.setStatus(_A)
_ZxAnQos3Dscp2CosProfileEntry_Object=MibTableRow
zxAnQos3Dscp2CosProfileEntry=_ZxAnQos3Dscp2CosProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,2,3,1))
zxAnQos3Dscp2CosProfileEntry.setIndexNames((0,_B,_Z))
if mibBuilder.loadTexts:zxAnQos3Dscp2CosProfileEntry.setStatus(_A)
class _ZxAnQosDscpToCosPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosDscpToCosPrfName_Type.__name__=_F
_ZxAnQosDscpToCosPrfName_Object=MibTableColumn
zxAnQosDscpToCosPrfName=_ZxAnQosDscpToCosPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,2,3,1,1),_ZxAnQosDscpToCosPrfName_Type())
zxAnQosDscpToCosPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosDscpToCosPrfName.setStatus(_A)
class _ZxAnQosDscpToCos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ZxAnQosDscpToCos_Type.__name__=_H
_ZxAnQosDscpToCos_Object=MibTableColumn
zxAnQosDscpToCos=_ZxAnQosDscpToCos_Object((1,3,6,1,4,1,3902,1015,21,4,2,3,1,2),_ZxAnQosDscpToCos_Type())
zxAnQosDscpToCos.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosDscpToCos.setStatus(_A)
_ZxAnQosDscpToCosPrfRowStatus_Type=RowStatus
_ZxAnQosDscpToCosPrfRowStatus_Object=MibTableColumn
zxAnQosDscpToCosPrfRowStatus=_ZxAnQosDscpToCosPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,2,3,1,20),_ZxAnQosDscpToCosPrfRowStatus_Type())
zxAnQosDscpToCosPrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosDscpToCosPrfRowStatus.setStatus(_A)
_ZxAnQos3Dscp2DropProfileTable_Object=MibTable
zxAnQos3Dscp2DropProfileTable=_ZxAnQos3Dscp2DropProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,2,4))
if mibBuilder.loadTexts:zxAnQos3Dscp2DropProfileTable.setStatus(_A)
_ZxAnQos3Dscp2DropProfileEntry_Object=MibTableRow
zxAnQos3Dscp2DropProfileEntry=_ZxAnQos3Dscp2DropProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,2,4,1))
zxAnQos3Dscp2DropProfileEntry.setIndexNames((0,_B,_a))
if mibBuilder.loadTexts:zxAnQos3Dscp2DropProfileEntry.setStatus(_A)
class _ZxAnQosDscpToDropPrecedePrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosDscpToDropPrecedePrfName_Type.__name__=_F
_ZxAnQosDscpToDropPrecedePrfName_Object=MibTableColumn
zxAnQosDscpToDropPrecedePrfName=_ZxAnQosDscpToDropPrecedePrfName_Object((1,3,6,1,4,1,3902,1015,21,4,2,4,1,1),_ZxAnQosDscpToDropPrecedePrfName_Type())
zxAnQosDscpToDropPrecedePrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosDscpToDropPrecedePrfName.setStatus(_A)
class _ZxAnQosDscpToDropPrecedence_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(64,64));fixedLength=64
_ZxAnQosDscpToDropPrecedence_Type.__name__=_H
_ZxAnQosDscpToDropPrecedence_Object=MibTableColumn
zxAnQosDscpToDropPrecedence=_ZxAnQosDscpToDropPrecedence_Object((1,3,6,1,4,1,3902,1015,21,4,2,4,1,2),_ZxAnQosDscpToDropPrecedence_Type())
zxAnQosDscpToDropPrecedence.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosDscpToDropPrecedence.setStatus(_A)
_ZxAnQosDscpToDropPrePrfRowStatus_Type=RowStatus
_ZxAnQosDscpToDropPrePrfRowStatus_Object=MibTableColumn
zxAnQosDscpToDropPrePrfRowStatus=_ZxAnQosDscpToDropPrePrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,2,4,1,20),_ZxAnQosDscpToDropPrePrfRowStatus_Type())
zxAnQosDscpToDropPrePrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosDscpToDropPrePrfRowStatus.setStatus(_A)
_ZxAnQos3MplsTc2CosProfileTable_Object=MibTable
zxAnQos3MplsTc2CosProfileTable=_ZxAnQos3MplsTc2CosProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,2,5))
if mibBuilder.loadTexts:zxAnQos3MplsTc2CosProfileTable.setStatus(_A)
_ZxAnQos3MplsTc2CosProfileEntry_Object=MibTableRow
zxAnQos3MplsTc2CosProfileEntry=_ZxAnQos3MplsTc2CosProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,2,5,1))
zxAnQos3MplsTc2CosProfileEntry.setIndexNames((0,_B,_b))
if mibBuilder.loadTexts:zxAnQos3MplsTc2CosProfileEntry.setStatus(_A)
class _ZxAnQosMplsTcToCosPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosMplsTcToCosPrfName_Type.__name__=_F
_ZxAnQosMplsTcToCosPrfName_Object=MibTableColumn
zxAnQosMplsTcToCosPrfName=_ZxAnQosMplsTcToCosPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,2,5,1,1),_ZxAnQosMplsTcToCosPrfName_Type())
zxAnQosMplsTcToCosPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosMplsTcToCosPrfName.setStatus(_A)
class _ZxAnQosMplsTcToCos_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosMplsTcToCos_Type.__name__=_H
_ZxAnQosMplsTcToCos_Object=MibTableColumn
zxAnQosMplsTcToCos=_ZxAnQosMplsTcToCos_Object((1,3,6,1,4,1,3902,1015,21,4,2,5,1,2),_ZxAnQosMplsTcToCos_Type())
zxAnQosMplsTcToCos.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosMplsTcToCos.setStatus(_A)
_ZxAnQosMplsTcToCosPrfRowStatus_Type=RowStatus
_ZxAnQosMplsTcToCosPrfRowStatus_Object=MibTableColumn
zxAnQosMplsTcToCosPrfRowStatus=_ZxAnQosMplsTcToCosPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,2,5,1,20),_ZxAnQosMplsTcToCosPrfRowStatus_Type())
zxAnQosMplsTcToCosPrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosMplsTcToCosPrfRowStatus.setStatus(_A)
_ZxAnQos3Cos2MplsTcProfileTable_Object=MibTable
zxAnQos3Cos2MplsTcProfileTable=_ZxAnQos3Cos2MplsTcProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,2,6))
if mibBuilder.loadTexts:zxAnQos3Cos2MplsTcProfileTable.setStatus(_A)
_ZxAnQos3Cos2MplsTcProfileEntry_Object=MibTableRow
zxAnQos3Cos2MplsTcProfileEntry=_ZxAnQos3Cos2MplsTcProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,2,6,1))
zxAnQos3Cos2MplsTcProfileEntry.setIndexNames((0,_B,_c))
if mibBuilder.loadTexts:zxAnQos3Cos2MplsTcProfileEntry.setStatus(_A)
class _ZxAnQosCosToMplsTcPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosCosToMplsTcPrfName_Type.__name__=_F
_ZxAnQosCosToMplsTcPrfName_Object=MibTableColumn
zxAnQosCosToMplsTcPrfName=_ZxAnQosCosToMplsTcPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,2,6,1,1),_ZxAnQosCosToMplsTcPrfName_Type())
zxAnQosCosToMplsTcPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosCosToMplsTcPrfName.setStatus(_A)
class _ZxAnQosCosToMplsTc_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosCosToMplsTc_Type.__name__=_H
_ZxAnQosCosToMplsTc_Object=MibTableColumn
zxAnQosCosToMplsTc=_ZxAnQosCosToMplsTc_Object((1,3,6,1,4,1,3902,1015,21,4,2,6,1,2),_ZxAnQosCosToMplsTc_Type())
zxAnQosCosToMplsTc.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosCosToMplsTc.setStatus(_A)
_ZxAnQosCosToMplsTcPrfRowStatus_Type=RowStatus
_ZxAnQosCosToMplsTcPrfRowStatus_Object=MibTableColumn
zxAnQosCosToMplsTcPrfRowStatus=_ZxAnQosCosToMplsTcPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,2,6,1,20),_ZxAnQosCosToMplsTcPrfRowStatus_Type())
zxAnQosCosToMplsTcPrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosCosToMplsTcPrfRowStatus.setStatus(_A)
_ZxAnQos3PortConfig_ObjectIdentity=ObjectIdentity
zxAnQos3PortConfig=_ZxAnQos3PortConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,4,3))
_ZxAnQos3PortConfigTable_Object=MibTable
zxAnQos3PortConfigTable=_ZxAnQos3PortConfigTable_Object((1,3,6,1,4,1,3902,1015,21,4,3,1))
if mibBuilder.loadTexts:zxAnQos3PortConfigTable.setStatus(_A)
_ZxAnQos3PortConfigEntry_Object=MibTableRow
zxAnQos3PortConfigEntry=_ZxAnQos3PortConfigEntry_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1))
zxAnQos3PortConfigEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:zxAnQos3PortConfigEntry.setStatus(_A)
_ZxAnQos3Rack_Type=Integer32
_ZxAnQos3Rack_Object=MibTableColumn
zxAnQos3Rack=_ZxAnQos3Rack_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,1),_ZxAnQos3Rack_Type())
zxAnQos3Rack.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQos3Rack.setStatus(_A)
_ZxAnQos3Shelf_Type=Integer32
_ZxAnQos3Shelf_Object=MibTableColumn
zxAnQos3Shelf=_ZxAnQos3Shelf_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,2),_ZxAnQos3Shelf_Type())
zxAnQos3Shelf.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQos3Shelf.setStatus(_A)
_ZxAnQos3Slot_Type=Integer32
_ZxAnQos3Slot_Object=MibTableColumn
zxAnQos3Slot=_ZxAnQos3Slot_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,3),_ZxAnQos3Slot_Type())
zxAnQos3Slot.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQos3Slot.setStatus(_A)
_ZxAnQos3Port_Type=Integer32
_ZxAnQos3Port_Object=MibTableColumn
zxAnQos3Port=_ZxAnQos3Port_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,4),_ZxAnQos3Port_Type())
zxAnQos3Port.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQos3Port.setStatus(_A)
_ZxAnQos3Onu_Type=Integer32
_ZxAnQos3Onu_Object=MibTableColumn
zxAnQos3Onu=_ZxAnQos3Onu_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,5),_ZxAnQos3Onu_Type())
zxAnQos3Onu.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQos3Onu.setStatus(_A)
class _ZxAnQos3VCircuitType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,11,12,13)));namedValues=NamedValues(*(('physicalPort',1),('bridgePort',2),('eponOnu',3),('gpon',4),(_d,11),('vlan',12),('queue',13)))
_ZxAnQos3VCircuitType_Type.__name__=_D
_ZxAnQos3VCircuitType_Object=MibTableColumn
zxAnQos3VCircuitType=_ZxAnQos3VCircuitType_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,6),_ZxAnQos3VCircuitType_Type())
zxAnQos3VCircuitType.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQos3VCircuitType.setStatus(_A)
_ZxAnQos3LogicalId_Type=ObjectIdentifier
_ZxAnQos3LogicalId_Object=MibTableColumn
zxAnQos3LogicalId=_ZxAnQos3LogicalId_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,7),_ZxAnQos3LogicalId_Type())
zxAnQos3LogicalId.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQos3LogicalId.setStatus(_A)
class _ZxAnQosIfRateLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,10000000))
_ZxAnQosIfRateLimit_Type.__name__=_D
_ZxAnQosIfRateLimit_Object=MibTableColumn
zxAnQosIfRateLimit=_ZxAnQosIfRateLimit_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,8),_ZxAnQosIfRateLimit_Type())
zxAnQosIfRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIfRateLimit.setUnits(_I)
class _ZxAnQosIfBucketSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4,16000))
_ZxAnQosIfBucketSize_Type.__name__=_D
_ZxAnQosIfBucketSize_Object=MibTableColumn
zxAnQosIfBucketSize=_ZxAnQosIfBucketSize_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,9),_ZxAnQosIfBucketSize_Type())
zxAnQosIfBucketSize.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfBucketSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIfBucketSize.setUnits(_Q)
class _ZxAnQosIfTrustMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('cos',1),('dscp',2)))
_ZxAnQosIfTrustMode_Type.__name__=_D
_ZxAnQosIfTrustMode_Object=MibTableColumn
zxAnQosIfTrustMode=_ZxAnQosIfTrustMode_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,10),_ZxAnQosIfTrustMode_Type())
zxAnQosIfTrustMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfTrustMode.setStatus(_A)
class _ZxAnQosIfDefaultCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7))
_ZxAnQosIfDefaultCos_Type.__name__=_D
_ZxAnQosIfDefaultCos_Object=MibTableColumn
zxAnQosIfDefaultCos=_ZxAnQosIfDefaultCos_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,11),_ZxAnQosIfDefaultCos_Type())
zxAnQosIfDefaultCos.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfDefaultCos.setStatus(_A)
class _ZxAnQosIfDscpToCosPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosIfDscpToCosPrf_Type.__name__=_F
_ZxAnQosIfDscpToCosPrf_Object=MibTableColumn
zxAnQosIfDscpToCosPrf=_ZxAnQosIfDscpToCosPrf_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,12),_ZxAnQosIfDscpToCosPrf_Type())
zxAnQosIfDscpToCosPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfDscpToCosPrf.setStatus(_A)
class _ZxAnQosIfDscpToDropPrecedencePrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIfDscpToDropPrecedencePrf_Type.__name__=_F
_ZxAnQosIfDscpToDropPrecedencePrf_Object=MibTableColumn
zxAnQosIfDscpToDropPrecedencePrf=_ZxAnQosIfDscpToDropPrecedencePrf_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,13),_ZxAnQosIfDscpToDropPrecedencePrf_Type())
zxAnQosIfDscpToDropPrecedencePrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfDscpToDropPrecedencePrf.setStatus(_A)
class _ZxAnQosIfDscpToDscpPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIfDscpToDscpPrf_Type.__name__=_F
_ZxAnQosIfDscpToDscpPrf_Object=MibTableColumn
zxAnQosIfDscpToDscpPrf=_ZxAnQosIfDscpToDscpPrf_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,14),_ZxAnQosIfDscpToDscpPrf_Type())
zxAnQosIfDscpToDscpPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfDscpToDscpPrf.setStatus(_A)
class _ZxAnQosIfIngressRateLimit_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(64,10000000))
_ZxAnQosIfIngressRateLimit_Type.__name__=_D
_ZxAnQosIfIngressRateLimit_Object=MibTableColumn
zxAnQosIfIngressRateLimit=_ZxAnQosIfIngressRateLimit_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,15),_ZxAnQosIfIngressRateLimit_Type())
zxAnQosIfIngressRateLimit.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfIngressRateLimit.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIfIngressRateLimit.setUnits(_I)
class _ZxAnQosIfIngressBucketSize_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(4,16000))
_ZxAnQosIfIngressBucketSize_Type.__name__=_D
_ZxAnQosIfIngressBucketSize_Object=MibTableColumn
zxAnQosIfIngressBucketSize=_ZxAnQosIfIngressBucketSize_Object((1,3,6,1,4,1,3902,1015,21,4,3,1,1,16),_ZxAnQosIfIngressBucketSize_Type())
zxAnQosIfIngressBucketSize.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfIngressBucketSize.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosIfIngressBucketSize.setUnits(_Q)
_ZxAnQos3VPortConfig_ObjectIdentity=ObjectIdentity
zxAnQos3VPortConfig=_ZxAnQos3VPortConfig_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,4,4))
_ZxAnQos3VPortConfigTable_Object=MibTable
zxAnQos3VPortConfigTable=_ZxAnQos3VPortConfigTable_Object((1,3,6,1,4,1,3902,1015,21,4,4,1))
if mibBuilder.loadTexts:zxAnQos3VPortConfigTable.setStatus(_A)
_ZxAnQos3VPortConfigEntry_Object=MibTableRow
zxAnQos3VPortConfigEntry=_ZxAnQos3VPortConfigEntry_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1))
zxAnQos3VPortConfigEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:zxAnQos3VPortConfigEntry.setStatus(_A)
class _ZxAnQosIfCosFilter_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,255)));namedValues=NamedValues(*(('enable',1),('disable',2),(_R,255)))
_ZxAnQosIfCosFilter_Type.__name__=_D
_ZxAnQosIfCosFilter_Object=MibTableColumn
zxAnQosIfCosFilter=_ZxAnQosIfCosFilter_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,1),_ZxAnQosIfCosFilter_Type())
zxAnQosIfCosFilter.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfCosFilter.setStatus(_A)
class _ZxAnQos3IngressCosMarkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),(_R,255)))
_ZxAnQos3IngressCosMarkMode_Type.__name__=_D
_ZxAnQos3IngressCosMarkMode_Object=MibTableColumn
zxAnQos3IngressCosMarkMode=_ZxAnQos3IngressCosMarkMode_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,2),_ZxAnQos3IngressCosMarkMode_Type())
zxAnQos3IngressCosMarkMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQos3IngressCosMarkMode.setStatus(_A)
class _ZxAnQos3IngressInnerCosMarkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),(_R,255)))
_ZxAnQos3IngressInnerCosMarkMode_Type.__name__=_D
_ZxAnQos3IngressInnerCosMarkMode_Object=MibTableColumn
zxAnQos3IngressInnerCosMarkMode=_ZxAnQos3IngressInnerCosMarkMode_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,3),_ZxAnQos3IngressInnerCosMarkMode_Type())
zxAnQos3IngressInnerCosMarkMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQos3IngressInnerCosMarkMode.setStatus(_A)
class _ZxAnQos3EgressCosMarkMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,255)));namedValues=NamedValues(*((_T,1),(_U,2),(_V,3),(_W,4),(_R,255)))
_ZxAnQos3EgressCosMarkMode_Type.__name__=_D
_ZxAnQos3EgressCosMarkMode_Object=MibTableColumn
zxAnQos3EgressCosMarkMode=_ZxAnQos3EgressCosMarkMode_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,4),_ZxAnQos3EgressCosMarkMode_Type())
zxAnQos3EgressCosMarkMode.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQos3EgressCosMarkMode.setStatus(_A)
class _ZxAnQos3IngressDefaultCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQos3IngressDefaultCos_Type.__name__=_D
_ZxAnQos3IngressDefaultCos_Object=MibTableColumn
zxAnQos3IngressDefaultCos=_ZxAnQos3IngressDefaultCos_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,5),_ZxAnQos3IngressDefaultCos_Type())
zxAnQos3IngressDefaultCos.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQos3IngressDefaultCos.setStatus(_A)
class _ZxAnQos3IngressDefaultInnerCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQos3IngressDefaultInnerCos_Type.__name__=_D
_ZxAnQos3IngressDefaultInnerCos_Object=MibTableColumn
zxAnQos3IngressDefaultInnerCos=_ZxAnQos3IngressDefaultInnerCos_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,6),_ZxAnQos3IngressDefaultInnerCos_Type())
zxAnQos3IngressDefaultInnerCos.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQos3IngressDefaultInnerCos.setStatus(_A)
class _ZxAnQosIfDefaultEgressCos_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosIfDefaultEgressCos_Type.__name__=_D
_ZxAnQosIfDefaultEgressCos_Object=MibTableColumn
zxAnQosIfDefaultEgressCos=_ZxAnQosIfDefaultEgressCos_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,7),_ZxAnQosIfDefaultEgressCos_Type())
zxAnQosIfDefaultEgressCos.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfDefaultEgressCos.setStatus(_A)
class _ZxAnQosIfCosToCosPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIfCosToCosPrf_Type.__name__=_F
_ZxAnQosIfCosToCosPrf_Object=MibTableColumn
zxAnQosIfCosToCosPrf=_ZxAnQosIfCosToCosPrf_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,8),_ZxAnQosIfCosToCosPrf_Type())
zxAnQosIfCosToCosPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfCosToCosPrf.setStatus(_A)
class _ZxAnQosIfCtagCosToCosPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIfCtagCosToCosPrf_Type.__name__=_F
_ZxAnQosIfCtagCosToCosPrf_Object=MibTableColumn
zxAnQosIfCtagCosToCosPrf=_ZxAnQosIfCtagCosToCosPrf_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,9),_ZxAnQosIfCtagCosToCosPrf_Type())
zxAnQosIfCtagCosToCosPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfCtagCosToCosPrf.setStatus(_A)
class _ZxAnQosIfEgressCosToCosPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIfEgressCosToCosPrf_Type.__name__=_F
_ZxAnQosIfEgressCosToCosPrf_Object=MibTableColumn
zxAnQosIfEgressCosToCosPrf=_ZxAnQosIfEgressCosToCosPrf_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,10),_ZxAnQosIfEgressCosToCosPrf_Type())
zxAnQosIfEgressCosToCosPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfEgressCosToCosPrf.setStatus(_A)
class _ZxAnQos3IngressDscp2CosPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQos3IngressDscp2CosPrf_Type.__name__=_F
_ZxAnQos3IngressDscp2CosPrf_Object=MibTableColumn
zxAnQos3IngressDscp2CosPrf=_ZxAnQos3IngressDscp2CosPrf_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,11),_ZxAnQos3IngressDscp2CosPrf_Type())
zxAnQos3IngressDscp2CosPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQos3IngressDscp2CosPrf.setStatus(_A)
class _ZxAnQos3IngressDscp2InnerCosPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQos3IngressDscp2InnerCosPrf_Type.__name__=_F
_ZxAnQos3IngressDscp2InnerCosPrf_Object=MibTableColumn
zxAnQos3IngressDscp2InnerCosPrf=_ZxAnQos3IngressDscp2InnerCosPrf_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,12),_ZxAnQos3IngressDscp2InnerCosPrf_Type())
zxAnQos3IngressDscp2InnerCosPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQos3IngressDscp2InnerCosPrf.setStatus(_A)
class _ZxAnQosIfEgressDscpToCosPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIfEgressDscpToCosPrf_Type.__name__=_F
_ZxAnQosIfEgressDscpToCosPrf_Object=MibTableColumn
zxAnQosIfEgressDscpToCosPrf=_ZxAnQosIfEgressDscpToCosPrf_Object((1,3,6,1,4,1,3902,1015,21,4,4,1,1,13),_ZxAnQosIfEgressDscpToCosPrf_Type())
zxAnQosIfEgressDscpToCosPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfEgressDscpToCosPrf.setStatus(_A)
_ZxAnQos3Queue_ObjectIdentity=ObjectIdentity
zxAnQos3Queue=_ZxAnQos3Queue_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,4,5))
_ZxAnQos3QueueBlockProfileTable_Object=MibTable
zxAnQos3QueueBlockProfileTable=_ZxAnQos3QueueBlockProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,5,1))
if mibBuilder.loadTexts:zxAnQos3QueueBlockProfileTable.setStatus(_A)
_ZxAnQos3QueueBlockProfileEntry_Object=MibTableRow
zxAnQos3QueueBlockProfileEntry=_ZxAnQos3QueueBlockProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,5,1,1))
zxAnQos3QueueBlockProfileEntry.setIndexNames((0,_B,_e))
if mibBuilder.loadTexts:zxAnQos3QueueBlockProfileEntry.setStatus(_A)
class _ZxAnQosQueueBlockPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosQueueBlockPrfName_Type.__name__=_F
_ZxAnQosQueueBlockPrfName_Object=MibTableColumn
zxAnQosQueueBlockPrfName=_ZxAnQosQueueBlockPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,5,1,1,1),_ZxAnQosQueueBlockPrfName_Type())
zxAnQosQueueBlockPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosQueueBlockPrfName.setStatus(_A)
class _ZxAnQosQueueBlockQNumber_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,8)));namedValues=NamedValues(*(('two',2),('four',4),('eight',8)))
_ZxAnQosQueueBlockQNumber_Type.__name__=_D
_ZxAnQosQueueBlockQNumber_Object=MibTableColumn
zxAnQosQueueBlockQNumber=_ZxAnQosQueueBlockQNumber_Object((1,3,6,1,4,1,3902,1015,21,4,5,1,1,2),_ZxAnQosQueueBlockQNumber_Type())
zxAnQosQueueBlockQNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosQueueBlockQNumber.setStatus(_A)
class _ZxAnQosQueueWeight_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosQueueWeight_Type.__name__=_H
_ZxAnQosQueueWeight_Object=MibTableColumn
zxAnQosQueueWeight=_ZxAnQosQueueWeight_Object((1,3,6,1,4,1,3902,1015,21,4,5,1,1,3),_ZxAnQosQueueWeight_Type())
zxAnQosQueueWeight.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosQueueWeight.setStatus(_A)
class _ZxAnQosQueueDepth_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosQueueDepth_Type.__name__=_H
_ZxAnQosQueueDepth_Object=MibTableColumn
zxAnQosQueueDepth=_ZxAnQosQueueDepth_Object((1,3,6,1,4,1,3902,1015,21,4,5,1,1,4),_ZxAnQosQueueDepth_Type())
zxAnQosQueueDepth.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosQueueDepth.setStatus(_A)
_ZxAnQosQueueBlockRowStatus_Type=RowStatus
_ZxAnQosQueueBlockRowStatus_Object=MibTableColumn
zxAnQosQueueBlockRowStatus=_ZxAnQosQueueBlockRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,5,1,1,20),_ZxAnQosQueueBlockRowStatus_Type())
zxAnQosQueueBlockRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosQueueBlockRowStatus.setStatus(_A)
_ZxAnQos3QueueMapProfileTable_Object=MibTable
zxAnQos3QueueMapProfileTable=_ZxAnQos3QueueMapProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,5,2))
if mibBuilder.loadTexts:zxAnQos3QueueMapProfileTable.setStatus(_A)
_ZxAnQos3QueueMapProfileEntry_Object=MibTableRow
zxAnQos3QueueMapProfileEntry=_ZxAnQos3QueueMapProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,5,2,1))
zxAnQos3QueueMapProfileEntry.setIndexNames((0,_B,_f))
if mibBuilder.loadTexts:zxAnQos3QueueMapProfileEntry.setStatus(_A)
class _ZxAnQosQueueMapPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosQueueMapPrfName_Type.__name__=_F
_ZxAnQosQueueMapPrfName_Object=MibTableColumn
zxAnQosQueueMapPrfName=_ZxAnQosQueueMapPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,5,2,1,1),_ZxAnQosQueueMapPrfName_Type())
zxAnQosQueueMapPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosQueueMapPrfName.setStatus(_A)
class _ZxAnQosQueueMapQNumber_Type(Integer32):defaultValue=8;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,4,8)));namedValues=NamedValues(*(('two',2),('four',4),('eight',8)))
_ZxAnQosQueueMapQNumber_Type.__name__=_D
_ZxAnQosQueueMapQNumber_Object=MibTableColumn
zxAnQosQueueMapQNumber=_ZxAnQosQueueMapQNumber_Object((1,3,6,1,4,1,3902,1015,21,4,5,2,1,2),_ZxAnQosQueueMapQNumber_Type())
zxAnQosQueueMapQNumber.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosQueueMapQNumber.setStatus(_A)
class _ZxAnQosQueueMapMode_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('cos',1),(_d,2),('gemPort',3),('pvc',4)))
_ZxAnQosQueueMapMode_Type.__name__=_D
_ZxAnQosQueueMapMode_Object=MibTableColumn
zxAnQosQueueMapMode=_ZxAnQosQueueMapMode_Object((1,3,6,1,4,1,3902,1015,21,4,5,2,1,3),_ZxAnQosQueueMapMode_Type())
zxAnQosQueueMapMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosQueueMapMode.setStatus(_A)
class _ZxAnQosCosToQueue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosCosToQueue_Type.__name__=_H
_ZxAnQosCosToQueue_Object=MibTableColumn
zxAnQosCosToQueue=_ZxAnQosCosToQueue_Object((1,3,6,1,4,1,3902,1015,21,4,5,2,1,4),_ZxAnQosCosToQueue_Type())
zxAnQosCosToQueue.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosCosToQueue.setStatus(_A)
class _ZxAnQosPvc2Queue_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(8,8));fixedLength=8
_ZxAnQosPvc2Queue_Type.__name__=_H
_ZxAnQosPvc2Queue_Object=MibTableColumn
zxAnQosPvc2Queue=_ZxAnQosPvc2Queue_Object((1,3,6,1,4,1,3902,1015,21,4,5,2,1,5),_ZxAnQosPvc2Queue_Type())
zxAnQosPvc2Queue.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosPvc2Queue.setStatus(_A)
_ZxAnQosQueueMapRowStatus_Type=RowStatus
_ZxAnQosQueueMapRowStatus_Object=MibTableColumn
zxAnQosQueueMapRowStatus=_ZxAnQosQueueMapRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,5,2,1,20),_ZxAnQosQueueMapRowStatus_Type())
zxAnQosQueueMapRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosQueueMapRowStatus.setStatus(_A)
_ZxAnQos3PortQueueConfigTable_Object=MibTable
zxAnQos3PortQueueConfigTable=_ZxAnQos3PortQueueConfigTable_Object((1,3,6,1,4,1,3902,1015,21,4,5,3))
if mibBuilder.loadTexts:zxAnQos3PortQueueConfigTable.setStatus(_A)
_ZxAnQos3PortQueueConfigEntry_Object=MibTableRow
zxAnQos3PortQueueConfigEntry=_ZxAnQos3PortQueueConfigEntry_Object((1,3,6,1,4,1,3902,1015,21,4,5,3,1))
zxAnQos3PortQueueConfigEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:zxAnQos3PortQueueConfigEntry.setStatus(_A)
class _ZxAnQosIfQueueBlockPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIfQueueBlockPrf_Type.__name__=_F
_ZxAnQosIfQueueBlockPrf_Object=MibTableColumn
zxAnQosIfQueueBlockPrf=_ZxAnQosIfQueueBlockPrf_Object((1,3,6,1,4,1,3902,1015,21,4,5,3,1,1),_ZxAnQosIfQueueBlockPrf_Type())
zxAnQosIfQueueBlockPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfQueueBlockPrf.setStatus(_A)
class _ZxAnQosIfQueueMapPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_ZxAnQosIfQueueMapPrf_Type.__name__=_F
_ZxAnQosIfQueueMapPrf_Object=MibTableColumn
zxAnQosIfQueueMapPrf=_ZxAnQosIfQueueMapPrf_Object((1,3,6,1,4,1,3902,1015,21,4,5,3,1,2),_ZxAnQosIfQueueMapPrf_Type())
zxAnQosIfQueueMapPrf.setMaxAccess(_E)
if mibBuilder.loadTexts:zxAnQosIfQueueMapPrf.setStatus(_A)
_ZxAnQos3Traffic_ObjectIdentity=ObjectIdentity
zxAnQos3Traffic=_ZxAnQos3Traffic_ObjectIdentity((1,3,6,1,4,1,3902,1015,21,4,6))
_ZxAnQos3TrafficProfileTable_Object=MibTable
zxAnQos3TrafficProfileTable=_ZxAnQos3TrafficProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,6,1))
if mibBuilder.loadTexts:zxAnQos3TrafficProfileTable.setStatus(_A)
_ZxAnQos3TrafficProfileEntry_Object=MibTableRow
zxAnQos3TrafficProfileEntry=_ZxAnQos3TrafficProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1))
zxAnQos3TrafficProfileEntry.setIndexNames((0,_B,_g))
if mibBuilder.loadTexts:zxAnQos3TrafficProfileEntry.setStatus(_A)
class _ZxAnQosTrafficPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosTrafficPrfName_Type.__name__=_F
_ZxAnQosTrafficPrfName_Object=MibTableColumn
zxAnQosTrafficPrfName=_ZxAnQosTrafficPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,1),_ZxAnQosTrafficPrfName_Type())
zxAnQosTrafficPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosTrafficPrfName.setStatus(_A)
class _ZxAnQosTrafficPrfCir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_ZxAnQosTrafficPrfCir_Type.__name__=_D
_ZxAnQosTrafficPrfCir_Object=MibTableColumn
zxAnQosTrafficPrfCir=_ZxAnQosTrafficPrfCir_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,2),_ZxAnQosTrafficPrfCir_Type())
zxAnQosTrafficPrfCir.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfCir.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosTrafficPrfCir.setUnits(_I)
class _ZxAnQosTrafficPrfCbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_ZxAnQosTrafficPrfCbs_Type.__name__=_D
_ZxAnQosTrafficPrfCbs_Object=MibTableColumn
zxAnQosTrafficPrfCbs=_ZxAnQosTrafficPrfCbs_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,3),_ZxAnQosTrafficPrfCbs_Type())
zxAnQosTrafficPrfCbs.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfCbs.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosTrafficPrfCbs.setUnits(_Q)
class _ZxAnQosTrafficPrfPir_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,10000000))
_ZxAnQosTrafficPrfPir_Type.__name__=_D
_ZxAnQosTrafficPrfPir_Object=MibTableColumn
zxAnQosTrafficPrfPir=_ZxAnQosTrafficPrfPir_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,4),_ZxAnQosTrafficPrfPir_Type())
zxAnQosTrafficPrfPir.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfPir.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosTrafficPrfPir.setUnits(_I)
class _ZxAnQosTrafficPrfPbs_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,1023))
_ZxAnQosTrafficPrfPbs_Type.__name__=_D
_ZxAnQosTrafficPrfPbs_Object=MibTableColumn
zxAnQosTrafficPrfPbs=_ZxAnQosTrafficPrfPbs_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,5),_ZxAnQosTrafficPrfPbs_Type())
zxAnQosTrafficPrfPbs.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfPbs.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosTrafficPrfPbs.setUnits(_Q)
class _ZxAnQosTrafficPrfDiscardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_ZxAnQosTrafficPrfDiscardMode_Type.__name__=_D
_ZxAnQosTrafficPrfDiscardMode_Object=MibTableColumn
zxAnQosTrafficPrfDiscardMode=_ZxAnQosTrafficPrfDiscardMode_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,6),_ZxAnQosTrafficPrfDiscardMode_Type())
zxAnQosTrafficPrfDiscardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfDiscardMode.setStatus(_A)
class _ZxAnQosTrafficPrfCirCosRemark_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosTrafficPrfCirCosRemark_Type.__name__=_D
_ZxAnQosTrafficPrfCirCosRemark_Object=MibTableColumn
zxAnQosTrafficPrfCirCosRemark=_ZxAnQosTrafficPrfCirCosRemark_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,7),_ZxAnQosTrafficPrfCirCosRemark_Type())
zxAnQosTrafficPrfCirCosRemark.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfCirCosRemark.setStatus(_A)
class _ZxAnQosTrafficPrfPirCosRemark_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosTrafficPrfPirCosRemark_Type.__name__=_D
_ZxAnQosTrafficPrfPirCosRemark_Object=MibTableColumn
zxAnQosTrafficPrfPirCosRemark=_ZxAnQosTrafficPrfPirCosRemark_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,8),_ZxAnQosTrafficPrfPirCosRemark_Type())
zxAnQosTrafficPrfPirCosRemark.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfPirCosRemark.setStatus(_A)
class _ZxAnQosTrafficPrfColorMode_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('colorAware',1),('colorBlind',2)))
_ZxAnQosTrafficPrfColorMode_Type.__name__=_D
_ZxAnQosTrafficPrfColorMode_Object=MibTableColumn
zxAnQosTrafficPrfColorMode=_ZxAnQosTrafficPrfColorMode_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,9),_ZxAnQosTrafficPrfColorMode_Type())
zxAnQosTrafficPrfColorMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfColorMode.setStatus(_A)
_ZxAnQosTrafficPrfRowStatus_Type=RowStatus
_ZxAnQosTrafficPrfRowStatus_Object=MibTableColumn
zxAnQosTrafficPrfRowStatus=_ZxAnQosTrafficPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,6,1,1,20),_ZxAnQosTrafficPrfRowStatus_Type())
zxAnQosTrafficPrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficPrfRowStatus.setStatus(_A)
_ZxAnQos3TrafficConfigTable_Object=MibTable
zxAnQos3TrafficConfigTable=_ZxAnQos3TrafficConfigTable_Object((1,3,6,1,4,1,3902,1015,21,4,6,2))
if mibBuilder.loadTexts:zxAnQos3TrafficConfigTable.setStatus(_A)
_ZxAnQos3TrafficConfigEntry_Object=MibTableRow
zxAnQos3TrafficConfigEntry=_ZxAnQos3TrafficConfigEntry_Object((1,3,6,1,4,1,3902,1015,21,4,6,2,1))
zxAnQos3TrafficConfigEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P),(0,_B,_j))
if mibBuilder.loadTexts:zxAnQos3TrafficConfigEntry.setStatus(_A)
class _ZxAnQosTrafficIfVlanDirection_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_ZxAnQosTrafficIfVlanDirection_Type.__name__=_D
_ZxAnQosTrafficIfVlanDirection_Object=MibTableColumn
zxAnQosTrafficIfVlanDirection=_ZxAnQosTrafficIfVlanDirection_Object((1,3,6,1,4,1,3902,1015,21,4,6,2,1,1),_ZxAnQosTrafficIfVlanDirection_Type())
zxAnQosTrafficIfVlanDirection.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosTrafficIfVlanDirection.setStatus(_A)
class _ZxAnQosTrafficIfConfPrf_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosTrafficIfConfPrf_Type.__name__=_F
_ZxAnQosTrafficIfConfPrf_Object=MibTableColumn
zxAnQosTrafficIfConfPrf=_ZxAnQosTrafficIfConfPrf_Object((1,3,6,1,4,1,3902,1015,21,4,6,2,1,2),_ZxAnQosTrafficIfConfPrf_Type())
zxAnQosTrafficIfConfPrf.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficIfConfPrf.setStatus(_A)
class _ZxAnQosTrafficIfConfPrfType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ip',1),('atm',2)))
_ZxAnQosTrafficIfConfPrfType_Type.__name__=_D
_ZxAnQosTrafficIfConfPrfType_Object=MibTableColumn
zxAnQosTrafficIfConfPrfType=_ZxAnQosTrafficIfConfPrfType_Object((1,3,6,1,4,1,3902,1015,21,4,6,2,1,3),_ZxAnQosTrafficIfConfPrfType_Type())
zxAnQosTrafficIfConfPrfType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficIfConfPrfType.setStatus(_A)
_ZxAnQosTrafficIfRowStatus_Type=RowStatus
_ZxAnQosTrafficIfRowStatus_Object=MibTableColumn
zxAnQosTrafficIfRowStatus=_ZxAnQosTrafficIfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,6,2,1,20),_ZxAnQosTrafficIfRowStatus_Type())
zxAnQosTrafficIfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosTrafficIfRowStatus.setStatus(_A)
_ZxAnQos3AtmTrafficProfileTable_Object=MibTable
zxAnQos3AtmTrafficProfileTable=_ZxAnQos3AtmTrafficProfileTable_Object((1,3,6,1,4,1,3902,1015,21,4,6,3))
if mibBuilder.loadTexts:zxAnQos3AtmTrafficProfileTable.setStatus(_A)
_ZxAnQos3AtmTrafficProfileEntry_Object=MibTableRow
zxAnQos3AtmTrafficProfileEntry=_ZxAnQos3AtmTrafficProfileEntry_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1))
zxAnQos3AtmTrafficProfileEntry.setIndexNames((0,_B,_k))
if mibBuilder.loadTexts:zxAnQos3AtmTrafficProfileEntry.setStatus(_A)
class _ZxAnQosAtmTrafficPrfName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_ZxAnQosAtmTrafficPrfName_Type.__name__=_F
_ZxAnQosAtmTrafficPrfName_Object=MibTableColumn
zxAnQosAtmTrafficPrfName=_ZxAnQosAtmTrafficPrfName_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,1),_ZxAnQosAtmTrafficPrfName_Type())
zxAnQosAtmTrafficPrfName.setMaxAccess(_G)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfName.setStatus(_A)
class _ZxAnQosAtmTrafficPrfType_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('atmCbr',1),('atmUbr',2),('atmVbr',3)))
_ZxAnQosAtmTrafficPrfType_Type.__name__=_D
_ZxAnQosAtmTrafficPrfType_Object=MibTableColumn
zxAnQosAtmTrafficPrfType=_ZxAnQosAtmTrafficPrfType_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,2),_ZxAnQosAtmTrafficPrfType_Type())
zxAnQosAtmTrafficPrfType.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfType.setStatus(_A)
class _ZxAnQosAtmTrafficPrfPcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20480))
_ZxAnQosAtmTrafficPrfPcr_Type.__name__=_D
_ZxAnQosAtmTrafficPrfPcr_Object=MibTableColumn
zxAnQosAtmTrafficPrfPcr=_ZxAnQosAtmTrafficPrfPcr_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,3),_ZxAnQosAtmTrafficPrfPcr_Type())
zxAnQosAtmTrafficPrfPcr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfPcr.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfPcr.setUnits(_I)
class _ZxAnQosAtmTrafficPrfPcrCosRemark_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosAtmTrafficPrfPcrCosRemark_Type.__name__=_D
_ZxAnQosAtmTrafficPrfPcrCosRemark_Object=MibTableColumn
zxAnQosAtmTrafficPrfPcrCosRemark=_ZxAnQosAtmTrafficPrfPcrCosRemark_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,4),_ZxAnQosAtmTrafficPrfPcrCosRemark_Type())
zxAnQosAtmTrafficPrfPcrCosRemark.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfPcrCosRemark.setStatus(_A)
class _ZxAnQosAtmTrafficPrfMcr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20480))
_ZxAnQosAtmTrafficPrfMcr_Type.__name__=_D
_ZxAnQosAtmTrafficPrfMcr_Object=MibTableColumn
zxAnQosAtmTrafficPrfMcr=_ZxAnQosAtmTrafficPrfMcr_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,5),_ZxAnQosAtmTrafficPrfMcr_Type())
zxAnQosAtmTrafficPrfMcr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfMcr.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfMcr.setUnits(_I)
class _ZxAnQosAtmTrafficPrfMcrCosRemark_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosAtmTrafficPrfMcrCosRemark_Type.__name__=_D
_ZxAnQosAtmTrafficPrfMcrCosRemark_Object=MibTableColumn
zxAnQosAtmTrafficPrfMcrCosRemark=_ZxAnQosAtmTrafficPrfMcrCosRemark_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,6),_ZxAnQosAtmTrafficPrfMcrCosRemark_Type())
zxAnQosAtmTrafficPrfMcrCosRemark.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfMcrCosRemark.setStatus(_A)
class _ZxAnQosAtmTrafficPrfScr_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,20480))
_ZxAnQosAtmTrafficPrfScr_Type.__name__=_D
_ZxAnQosAtmTrafficPrfScr_Object=MibTableColumn
zxAnQosAtmTrafficPrfScr=_ZxAnQosAtmTrafficPrfScr_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,7),_ZxAnQosAtmTrafficPrfScr_Type())
zxAnQosAtmTrafficPrfScr.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfScr.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfScr.setUnits(_I)
class _ZxAnQosAtmTrafficPrfScrCosRemark_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_ZxAnQosAtmTrafficPrfScrCosRemark_Type.__name__=_D
_ZxAnQosAtmTrafficPrfScrCosRemark_Object=MibTableColumn
zxAnQosAtmTrafficPrfScrCosRemark=_ZxAnQosAtmTrafficPrfScrCosRemark_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,8),_ZxAnQosAtmTrafficPrfScrCosRemark_Type())
zxAnQosAtmTrafficPrfScrCosRemark.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfScrCosRemark.setStatus(_A)
class _ZxAnQosAtmTrafficPrfDiscardMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_h,1),(_i,2)))
_ZxAnQosAtmTrafficPrfDiscardMode_Type.__name__=_D
_ZxAnQosAtmTrafficPrfDiscardMode_Object=MibTableColumn
zxAnQosAtmTrafficPrfDiscardMode=_ZxAnQosAtmTrafficPrfDiscardMode_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,9),_ZxAnQosAtmTrafficPrfDiscardMode_Type())
zxAnQosAtmTrafficPrfDiscardMode.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfDiscardMode.setStatus(_A)
_ZxAnQosAtmTrafficPrfRowStatus_Type=RowStatus
_ZxAnQosAtmTrafficPrfRowStatus_Object=MibTableColumn
zxAnQosAtmTrafficPrfRowStatus=_ZxAnQosAtmTrafficPrfRowStatus_Object((1,3,6,1,4,1,3902,1015,21,4,6,3,1,20),_ZxAnQosAtmTrafficPrfRowStatus_Type())
zxAnQosAtmTrafficPrfRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:zxAnQosAtmTrafficPrfRowStatus.setStatus(_A)
_ZxAnQos3RemainingBwTable_Object=MibTable
zxAnQos3RemainingBwTable=_ZxAnQos3RemainingBwTable_Object((1,3,6,1,4,1,3902,1015,21,4,6,24))
if mibBuilder.loadTexts:zxAnQos3RemainingBwTable.setStatus(_A)
_ZxAnQos3RemainingBwEntry_Object=MibTableRow
zxAnQos3RemainingBwEntry=_ZxAnQos3RemainingBwEntry_Object((1,3,6,1,4,1,3902,1015,21,4,6,24,1))
zxAnQos3RemainingBwEntry.setIndexNames((0,_B,_J),(0,_B,_K),(0,_B,_L),(0,_B,_M),(0,_B,_N),(0,_B,_O),(0,_B,_P))
if mibBuilder.loadTexts:zxAnQos3RemainingBwEntry.setStatus(_A)
_ZxAnQosTrafficTotalBandwidth_Type=Integer32
_ZxAnQosTrafficTotalBandwidth_Object=MibTableColumn
zxAnQosTrafficTotalBandwidth=_ZxAnQosTrafficTotalBandwidth_Object((1,3,6,1,4,1,3902,1015,21,4,6,24,1,1),_ZxAnQosTrafficTotalBandwidth_Type())
zxAnQosTrafficTotalBandwidth.setMaxAccess(_S)
if mibBuilder.loadTexts:zxAnQosTrafficTotalBandwidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosTrafficTotalBandwidth.setUnits(_I)
_ZxAnQosTrafficRemainingBandwidth_Type=Integer32
_ZxAnQosTrafficRemainingBandwidth_Object=MibTableColumn
zxAnQosTrafficRemainingBandwidth=_ZxAnQosTrafficRemainingBandwidth_Object((1,3,6,1,4,1,3902,1015,21,4,6,24,1,2),_ZxAnQosTrafficRemainingBandwidth_Type())
zxAnQosTrafficRemainingBandwidth.setMaxAccess(_S)
if mibBuilder.loadTexts:zxAnQosTrafficRemainingBandwidth.setStatus(_A)
if mibBuilder.loadTexts:zxAnQosTrafficRemainingBandwidth.setUnits(_I)
mibBuilder.exportSymbols(_B,**{'zxAnQosMib':zxAnQosMib,'zxAnQos3Objects':zxAnQos3Objects,'zxAnQos3GlobalObjects':zxAnQos3GlobalObjects,'zxAnQos3MgmtCapabilities':zxAnQos3MgmtCapabilities,'zxAnQos3QueueGlobalObjects':zxAnQos3QueueGlobalObjects,'zxAnQosEthCosToQueue':zxAnQosEthCosToQueue,'zxAnQos3MappingProfile':zxAnQos3MappingProfile,'zxAnQos3CosRemarkProfileTable':zxAnQos3CosRemarkProfileTable,'zxAnQos3CosRemarkProfileEntry':zxAnQos3CosRemarkProfileEntry,_X:zxAnQosCosToCosPrfName,'zxAnQosCosToCos':zxAnQosCosToCos,'zxAnQosCosToCosPrfRowStatus':zxAnQosCosToCosPrfRowStatus,'zxAnQos3DscpRemarkProfileTable':zxAnQos3DscpRemarkProfileTable,'zxAnQos3DscpRemarkProfileEntry':zxAnQos3DscpRemarkProfileEntry,_Y:zxAnQosDscpToDscpPrfName,'zxAnQosDscpToDscp':zxAnQosDscpToDscp,'zxAnQosDscpToDscpPrfRowStatus':zxAnQosDscpToDscpPrfRowStatus,'zxAnQos3Dscp2CosProfileTable':zxAnQos3Dscp2CosProfileTable,'zxAnQos3Dscp2CosProfileEntry':zxAnQos3Dscp2CosProfileEntry,_Z:zxAnQosDscpToCosPrfName,'zxAnQosDscpToCos':zxAnQosDscpToCos,'zxAnQosDscpToCosPrfRowStatus':zxAnQosDscpToCosPrfRowStatus,'zxAnQos3Dscp2DropProfileTable':zxAnQos3Dscp2DropProfileTable,'zxAnQos3Dscp2DropProfileEntry':zxAnQos3Dscp2DropProfileEntry,_a:zxAnQosDscpToDropPrecedePrfName,'zxAnQosDscpToDropPrecedence':zxAnQosDscpToDropPrecedence,'zxAnQosDscpToDropPrePrfRowStatus':zxAnQosDscpToDropPrePrfRowStatus,'zxAnQos3MplsTc2CosProfileTable':zxAnQos3MplsTc2CosProfileTable,'zxAnQos3MplsTc2CosProfileEntry':zxAnQos3MplsTc2CosProfileEntry,_b:zxAnQosMplsTcToCosPrfName,'zxAnQosMplsTcToCos':zxAnQosMplsTcToCos,'zxAnQosMplsTcToCosPrfRowStatus':zxAnQosMplsTcToCosPrfRowStatus,'zxAnQos3Cos2MplsTcProfileTable':zxAnQos3Cos2MplsTcProfileTable,'zxAnQos3Cos2MplsTcProfileEntry':zxAnQos3Cos2MplsTcProfileEntry,_c:zxAnQosCosToMplsTcPrfName,'zxAnQosCosToMplsTc':zxAnQosCosToMplsTc,'zxAnQosCosToMplsTcPrfRowStatus':zxAnQosCosToMplsTcPrfRowStatus,'zxAnQos3PortConfig':zxAnQos3PortConfig,'zxAnQos3PortConfigTable':zxAnQos3PortConfigTable,'zxAnQos3PortConfigEntry':zxAnQos3PortConfigEntry,_J:zxAnQos3Rack,_K:zxAnQos3Shelf,_L:zxAnQos3Slot,_M:zxAnQos3Port,_N:zxAnQos3Onu,_O:zxAnQos3VCircuitType,_P:zxAnQos3LogicalId,'zxAnQosIfRateLimit':zxAnQosIfRateLimit,'zxAnQosIfBucketSize':zxAnQosIfBucketSize,'zxAnQosIfTrustMode':zxAnQosIfTrustMode,'zxAnQosIfDefaultCos':zxAnQosIfDefaultCos,'zxAnQosIfDscpToCosPrf':zxAnQosIfDscpToCosPrf,'zxAnQosIfDscpToDropPrecedencePrf':zxAnQosIfDscpToDropPrecedencePrf,'zxAnQosIfDscpToDscpPrf':zxAnQosIfDscpToDscpPrf,'zxAnQosIfIngressRateLimit':zxAnQosIfIngressRateLimit,'zxAnQosIfIngressBucketSize':zxAnQosIfIngressBucketSize,'zxAnQos3VPortConfig':zxAnQos3VPortConfig,'zxAnQos3VPortConfigTable':zxAnQos3VPortConfigTable,'zxAnQos3VPortConfigEntry':zxAnQos3VPortConfigEntry,'zxAnQosIfCosFilter':zxAnQosIfCosFilter,'zxAnQos3IngressCosMarkMode':zxAnQos3IngressCosMarkMode,'zxAnQos3IngressInnerCosMarkMode':zxAnQos3IngressInnerCosMarkMode,'zxAnQos3EgressCosMarkMode':zxAnQos3EgressCosMarkMode,'zxAnQos3IngressDefaultCos':zxAnQos3IngressDefaultCos,'zxAnQos3IngressDefaultInnerCos':zxAnQos3IngressDefaultInnerCos,'zxAnQosIfDefaultEgressCos':zxAnQosIfDefaultEgressCos,'zxAnQosIfCosToCosPrf':zxAnQosIfCosToCosPrf,'zxAnQosIfCtagCosToCosPrf':zxAnQosIfCtagCosToCosPrf,'zxAnQosIfEgressCosToCosPrf':zxAnQosIfEgressCosToCosPrf,'zxAnQos3IngressDscp2CosPrf':zxAnQos3IngressDscp2CosPrf,'zxAnQos3IngressDscp2InnerCosPrf':zxAnQos3IngressDscp2InnerCosPrf,'zxAnQosIfEgressDscpToCosPrf':zxAnQosIfEgressDscpToCosPrf,'zxAnQos3Queue':zxAnQos3Queue,'zxAnQos3QueueBlockProfileTable':zxAnQos3QueueBlockProfileTable,'zxAnQos3QueueBlockProfileEntry':zxAnQos3QueueBlockProfileEntry,_e:zxAnQosQueueBlockPrfName,'zxAnQosQueueBlockQNumber':zxAnQosQueueBlockQNumber,'zxAnQosQueueWeight':zxAnQosQueueWeight,'zxAnQosQueueDepth':zxAnQosQueueDepth,'zxAnQosQueueBlockRowStatus':zxAnQosQueueBlockRowStatus,'zxAnQos3QueueMapProfileTable':zxAnQos3QueueMapProfileTable,'zxAnQos3QueueMapProfileEntry':zxAnQos3QueueMapProfileEntry,_f:zxAnQosQueueMapPrfName,'zxAnQosQueueMapQNumber':zxAnQosQueueMapQNumber,'zxAnQosQueueMapMode':zxAnQosQueueMapMode,'zxAnQosCosToQueue':zxAnQosCosToQueue,'zxAnQosPvc2Queue':zxAnQosPvc2Queue,'zxAnQosQueueMapRowStatus':zxAnQosQueueMapRowStatus,'zxAnQos3PortQueueConfigTable':zxAnQos3PortQueueConfigTable,'zxAnQos3PortQueueConfigEntry':zxAnQos3PortQueueConfigEntry,'zxAnQosIfQueueBlockPrf':zxAnQosIfQueueBlockPrf,'zxAnQosIfQueueMapPrf':zxAnQosIfQueueMapPrf,'zxAnQos3Traffic':zxAnQos3Traffic,'zxAnQos3TrafficProfileTable':zxAnQos3TrafficProfileTable,'zxAnQos3TrafficProfileEntry':zxAnQos3TrafficProfileEntry,_g:zxAnQosTrafficPrfName,'zxAnQosTrafficPrfCir':zxAnQosTrafficPrfCir,'zxAnQosTrafficPrfCbs':zxAnQosTrafficPrfCbs,'zxAnQosTrafficPrfPir':zxAnQosTrafficPrfPir,'zxAnQosTrafficPrfPbs':zxAnQosTrafficPrfPbs,'zxAnQosTrafficPrfDiscardMode':zxAnQosTrafficPrfDiscardMode,'zxAnQosTrafficPrfCirCosRemark':zxAnQosTrafficPrfCirCosRemark,'zxAnQosTrafficPrfPirCosRemark':zxAnQosTrafficPrfPirCosRemark,'zxAnQosTrafficPrfColorMode':zxAnQosTrafficPrfColorMode,'zxAnQosTrafficPrfRowStatus':zxAnQosTrafficPrfRowStatus,'zxAnQos3TrafficConfigTable':zxAnQos3TrafficConfigTable,'zxAnQos3TrafficConfigEntry':zxAnQos3TrafficConfigEntry,_j:zxAnQosTrafficIfVlanDirection,'zxAnQosTrafficIfConfPrf':zxAnQosTrafficIfConfPrf,'zxAnQosTrafficIfConfPrfType':zxAnQosTrafficIfConfPrfType,'zxAnQosTrafficIfRowStatus':zxAnQosTrafficIfRowStatus,'zxAnQos3AtmTrafficProfileTable':zxAnQos3AtmTrafficProfileTable,'zxAnQos3AtmTrafficProfileEntry':zxAnQos3AtmTrafficProfileEntry,_k:zxAnQosAtmTrafficPrfName,'zxAnQosAtmTrafficPrfType':zxAnQosAtmTrafficPrfType,'zxAnQosAtmTrafficPrfPcr':zxAnQosAtmTrafficPrfPcr,'zxAnQosAtmTrafficPrfPcrCosRemark':zxAnQosAtmTrafficPrfPcrCosRemark,'zxAnQosAtmTrafficPrfMcr':zxAnQosAtmTrafficPrfMcr,'zxAnQosAtmTrafficPrfMcrCosRemark':zxAnQosAtmTrafficPrfMcrCosRemark,'zxAnQosAtmTrafficPrfScr':zxAnQosAtmTrafficPrfScr,'zxAnQosAtmTrafficPrfScrCosRemark':zxAnQosAtmTrafficPrfScrCosRemark,'zxAnQosAtmTrafficPrfDiscardMode':zxAnQosAtmTrafficPrfDiscardMode,'zxAnQosAtmTrafficPrfRowStatus':zxAnQosAtmTrafficPrfRowStatus,'zxAnQos3RemainingBwTable':zxAnQos3RemainingBwTable,'zxAnQos3RemainingBwEntry':zxAnQos3RemainingBwEntry,'zxAnQosTrafficTotalBandwidth':zxAnQosTrafficTotalBandwidth,'zxAnQosTrafficRemainingBandwidth':zxAnQosTrafficRemainingBandwidth})