_L='eltVlanMulticastTvEntry'
_K='read-create'
_J='not-accessible'
_I='eltVlanTriplePlayInputPort'
_H='eltVlanTriplePlayInnerVID'
_G='2013-11-18 00:00'
_F='Integer32'
_E='dot1qVlanIndex'
_D='Q-BRIDGE-MIB'
_C='ELTEX-MES-VLAN-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols('BRIDGE-MIB','dot1dBasePort')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
InterfaceIndexOrZero,ifIndex=mibBuilder.importSymbols('IF-MIB','InterfaceIndexOrZero','ifIndex')
InetAddressType,=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddressType')
PortList,VlanIndex,dot1qVlanIndex=mibBuilder.importSymbols(_D,'PortList','VlanIndex',_E)
rnd,=mibBuilder.importSymbols('RADLAN-MIB','rnd')
vlanMulticastTvEntry,=mibBuilder.importSymbols('RADLAN-vlan-MIB','vlanMulticastTvEntry')
SnmpAdminString,=mibBuilder.importSymbols('SNMP-FRAMEWORK-MIB','SnmpAdminString')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','RowStatus','TextualConvention','TruthValue')
eltMesVlan=ModuleIdentity((1,3,6,1,4,1,35265,1,23,5))
if mibBuilder.loadTexts:eltMesVlan.setRevisions(('2018-08-07 00:00','2017-06-05 00:00',_G,_G))
class EltVlanMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('basic',1),('tr101',2)))
_EltVlanMulticastTvTable_Object=MibTable
eltVlanMulticastTvTable=_EltVlanMulticastTvTable_Object((1,3,6,1,4,1,35265,1,23,5,1))
if mibBuilder.loadTexts:eltVlanMulticastTvTable.setStatus(_A)
_EltVlanMulticastTvEntry_Object=MibTableRow
eltVlanMulticastTvEntry=_EltVlanMulticastTvEntry_Object((1,3,6,1,4,1,35265,1,23,5,1,1))
if mibBuilder.loadTexts:eltVlanMulticastTvEntry.setStatus(_A)
_EltVlanMulticastTvVIDIsTagged_Type=TruthValue
_EltVlanMulticastTvVIDIsTagged_Object=MibTableColumn
eltVlanMulticastTvVIDIsTagged=_EltVlanMulticastTvVIDIsTagged_Object((1,3,6,1,4,1,35265,1,23,5,1,1,1),_EltVlanMulticastTvVIDIsTagged_Type())
eltVlanMulticastTvVIDIsTagged.setMaxAccess(_B)
if mibBuilder.loadTexts:eltVlanMulticastTvVIDIsTagged.setStatus(_A)
_EltVlanMode_Type=EltVlanMode
_EltVlanMode_Object=MibScalar
eltVlanMode=_EltVlanMode_Object((1,3,6,1,4,1,35265,1,23,5,2),_EltVlanMode_Type())
eltVlanMode.setMaxAccess(_B)
if mibBuilder.loadTexts:eltVlanMode.setStatus(_A)
_EltDot1qVlanStaticTable_Object=MibTable
eltDot1qVlanStaticTable=_EltDot1qVlanStaticTable_Object((1,3,6,1,4,1,35265,1,23,5,4))
if mibBuilder.loadTexts:eltDot1qVlanStaticTable.setStatus(_A)
_EltDot1qVlanStaticEntry_Object=MibTableRow
eltDot1qVlanStaticEntry=_EltDot1qVlanStaticEntry_Object((1,3,6,1,4,1,35265,1,23,5,4,1))
eltDot1qVlanStaticEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:eltDot1qVlanStaticEntry.setStatus(_A)
class _EltDot1qVlanStaticCos_Type(Integer32):defaultValue=255;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,7),ValueRangeConstraint(255,255))
_EltDot1qVlanStaticCos_Type.__name__=_F
_EltDot1qVlanStaticCos_Object=MibTableColumn
eltDot1qVlanStaticCos=_EltDot1qVlanStaticCos_Object((1,3,6,1,4,1,35265,1,23,5,4,1,1),_EltDot1qVlanStaticCos_Type())
eltDot1qVlanStaticCos.setMaxAccess(_B)
if mibBuilder.loadTexts:eltDot1qVlanStaticCos.setStatus(_A)
_EltMesVlanDefault_ObjectIdentity=ObjectIdentity
eltMesVlanDefault=_EltMesVlanDefault_ObjectIdentity((1,3,6,1,4,1,35265,1,23,5,5))
_EltVlanDefaultForbiddenPorts_Type=PortList
_EltVlanDefaultForbiddenPorts_Object=MibScalar
eltVlanDefaultForbiddenPorts=_EltVlanDefaultForbiddenPorts_Object((1,3,6,1,4,1,35265,1,23,5,5,1),_EltVlanDefaultForbiddenPorts_Type())
eltVlanDefaultForbiddenPorts.setMaxAccess(_B)
if mibBuilder.loadTexts:eltVlanDefaultForbiddenPorts.setStatus(_A)
_EltVlanTriplePlayTable_Object=MibTable
eltVlanTriplePlayTable=_EltVlanTriplePlayTable_Object((1,3,6,1,4,1,35265,1,23,5,6))
if mibBuilder.loadTexts:eltVlanTriplePlayTable.setStatus(_A)
_EltVlanTriplePlayEntry_Object=MibTableRow
eltVlanTriplePlayEntry=_EltVlanTriplePlayEntry_Object((1,3,6,1,4,1,35265,1,23,5,6,1))
eltVlanTriplePlayEntry.setIndexNames((0,_C,_H),(0,_C,_I))
if mibBuilder.loadTexts:eltVlanTriplePlayEntry.setStatus(_A)
_EltVlanTriplePlayInnerVID_Type=VlanIndex
_EltVlanTriplePlayInnerVID_Object=MibTableColumn
eltVlanTriplePlayInnerVID=_EltVlanTriplePlayInnerVID_Object((1,3,6,1,4,1,35265,1,23,5,6,1,1),_EltVlanTriplePlayInnerVID_Type())
eltVlanTriplePlayInnerVID.setMaxAccess(_J)
if mibBuilder.loadTexts:eltVlanTriplePlayInnerVID.setStatus(_A)
_EltVlanTriplePlayInputPort_Type=InterfaceIndexOrZero
_EltVlanTriplePlayInputPort_Object=MibTableColumn
eltVlanTriplePlayInputPort=_EltVlanTriplePlayInputPort_Object((1,3,6,1,4,1,35265,1,23,5,6,1,2),_EltVlanTriplePlayInputPort_Type())
eltVlanTriplePlayInputPort.setMaxAccess(_J)
if mibBuilder.loadTexts:eltVlanTriplePlayInputPort.setStatus(_A)
_EltVlanTriplePlayMulticastTvVID_Type=VlanIndex
_EltVlanTriplePlayMulticastTvVID_Object=MibTableColumn
eltVlanTriplePlayMulticastTvVID=_EltVlanTriplePlayMulticastTvVID_Object((1,3,6,1,4,1,35265,1,23,5,6,1,3),_EltVlanTriplePlayMulticastTvVID_Type())
eltVlanTriplePlayMulticastTvVID.setMaxAccess(_K)
if mibBuilder.loadTexts:eltVlanTriplePlayMulticastTvVID.setStatus(_A)
_EltVlanTriplePlayRowStatus_Type=RowStatus
_EltVlanTriplePlayRowStatus_Object=MibTableColumn
eltVlanTriplePlayRowStatus=_EltVlanTriplePlayRowStatus_Object((1,3,6,1,4,1,35265,1,23,5,6,1,4),_EltVlanTriplePlayRowStatus_Type())
eltVlanTriplePlayRowStatus.setMaxAccess(_K)
if mibBuilder.loadTexts:eltVlanTriplePlayRowStatus.setStatus(_A)
vlanMulticastTvEntry.registerAugmentions((_C,_L))
eltVlanMulticastTvEntry.setIndexNames(*vlanMulticastTvEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'EltVlanMode':EltVlanMode,'eltMesVlan':eltMesVlan,'eltVlanMulticastTvTable':eltVlanMulticastTvTable,_L:eltVlanMulticastTvEntry,'eltVlanMulticastTvVIDIsTagged':eltVlanMulticastTvVIDIsTagged,'eltVlanMode':eltVlanMode,'eltDot1qVlanStaticTable':eltDot1qVlanStaticTable,'eltDot1qVlanStaticEntry':eltDot1qVlanStaticEntry,'eltDot1qVlanStaticCos':eltDot1qVlanStaticCos,'eltMesVlanDefault':eltMesVlanDefault,'eltVlanDefaultForbiddenPorts':eltVlanDefaultForbiddenPorts,'eltVlanTriplePlayTable':eltVlanTriplePlayTable,'eltVlanTriplePlayEntry':eltVlanTriplePlayEntry,_H:eltVlanTriplePlayInnerVID,_I:eltVlanTriplePlayInputPort,'eltVlanTriplePlayMulticastTvVID':eltVlanTriplePlayMulticastTvVID,'eltVlanTriplePlayRowStatus':eltVlanTriplePlayRowStatus})