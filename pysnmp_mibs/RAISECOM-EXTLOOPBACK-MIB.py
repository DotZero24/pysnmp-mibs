_H='rcExtLoopbackPortIndex'
_G='RAISECOM-EXTLOOPBACK-MIB'
_F='Unsigned32'
_E='Integer32'
_D='Gauge32'
_C='Counter32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
iscomSwitch,=mibBuilder.importSymbols('RAISECOM-BASE-MIB','iscomSwitch')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits',_C,'Counter64',_D,_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_F,'iso')
Counter32,DisplayString,Gauge32,Integer32,MacAddress,PhysAddress,TextualConvention,Unsigned32=mibBuilder.importSymbols('SNMPv2-TC',_C,'DisplayString',_D,_E,'MacAddress','PhysAddress','TextualConvention',_F)
EnableVar,=mibBuilder.importSymbols('SWITCH-TC','EnableVar')
rcExtLoopback=ModuleIdentity((1,3,6,1,4,1,8886,6,1,45))
if mibBuilder.loadTexts:rcExtLoopback.setRevisions(('2007-11-02 00:00',))
class RcExtLoopbackMode(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6,7)));namedValues=NamedValues(*(('disable',1),('port',2),('dmac',3),('smac',4),('cvlan',5),('svlan',6),('dvlan',7)))
_RcExtloopbackObjectsGroup_ObjectIdentity=ObjectIdentity
rcExtloopbackObjectsGroup=_RcExtloopbackObjectsGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,45,1))
_RcExtLoopbackBMDMacTransEnable_Type=EnableVar
_RcExtLoopbackBMDMacTransEnable_Object=MibScalar
rcExtLoopbackBMDMacTransEnable=_RcExtLoopbackBMDMacTransEnable_Object((1,3,6,1,4,1,8886,6,1,45,1,1),_RcExtLoopbackBMDMacTransEnable_Type())
rcExtLoopbackBMDMacTransEnable.setMaxAccess(_B)
if mibBuilder.loadTexts:rcExtLoopbackBMDMacTransEnable.setStatus(_A)
_RcExtloopbackConfigGroup_ObjectIdentity=ObjectIdentity
rcExtloopbackConfigGroup=_RcExtloopbackConfigGroup_ObjectIdentity((1,3,6,1,4,1,8886,6,1,45,2))
_RcExtLoopbackTable_Object=MibTable
rcExtLoopbackTable=_RcExtLoopbackTable_Object((1,3,6,1,4,1,8886,6,1,45,2,1))
if mibBuilder.loadTexts:rcExtLoopbackTable.setStatus(_A)
_RcExtLoopbackEntry_Object=MibTableRow
rcExtLoopbackEntry=_RcExtLoopbackEntry_Object((1,3,6,1,4,1,8886,6,1,45,2,1,1))
rcExtLoopbackEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:rcExtLoopbackEntry.setStatus(_A)
_RcExtLoopbackPortIndex_Type=Integer32
_RcExtLoopbackPortIndex_Object=MibTableColumn
rcExtLoopbackPortIndex=_RcExtLoopbackPortIndex_Object((1,3,6,1,4,1,8886,6,1,45,2,1,1,1),_RcExtLoopbackPortIndex_Type())
rcExtLoopbackPortIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:rcExtLoopbackPortIndex.setStatus(_A)
_RcExtLoopbackDMac_Type=MacAddress
_RcExtLoopbackDMac_Object=MibTableColumn
rcExtLoopbackDMac=_RcExtLoopbackDMac_Object((1,3,6,1,4,1,8886,6,1,45,2,1,1,2),_RcExtLoopbackDMac_Type())
rcExtLoopbackDMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rcExtLoopbackDMac.setStatus(_A)
_RcExtLoopbackSMac_Type=MacAddress
_RcExtLoopbackSMac_Object=MibTableColumn
rcExtLoopbackSMac=_RcExtLoopbackSMac_Object((1,3,6,1,4,1,8886,6,1,45,2,1,1,3),_RcExtLoopbackSMac_Type())
rcExtLoopbackSMac.setMaxAccess(_B)
if mibBuilder.loadTexts:rcExtLoopbackSMac.setStatus(_A)
_RcExtLoopbackSVlan_Type=VlanId
_RcExtLoopbackSVlan_Object=MibTableColumn
rcExtLoopbackSVlan=_RcExtLoopbackSVlan_Object((1,3,6,1,4,1,8886,6,1,45,2,1,1,4),_RcExtLoopbackSVlan_Type())
rcExtLoopbackSVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcExtLoopbackSVlan.setStatus(_A)
_RcExtLoopbackCVlan_Type=VlanId
_RcExtLoopbackCVlan_Object=MibTableColumn
rcExtLoopbackCVlan=_RcExtLoopbackCVlan_Object((1,3,6,1,4,1,8886,6,1,45,2,1,1,5),_RcExtLoopbackCVlan_Type())
rcExtLoopbackCVlan.setMaxAccess(_B)
if mibBuilder.loadTexts:rcExtLoopbackCVlan.setStatus(_A)
_RcExtLoopbackTime_Type=Integer32
_RcExtLoopbackTime_Object=MibTableColumn
rcExtLoopbackTime=_RcExtLoopbackTime_Object((1,3,6,1,4,1,8886,6,1,45,2,1,1,6),_RcExtLoopbackTime_Type())
rcExtLoopbackTime.setMaxAccess(_B)
if mibBuilder.loadTexts:rcExtLoopbackTime.setStatus(_A)
_RcExtLoopbackMode_Type=RcExtLoopbackMode
_RcExtLoopbackMode_Object=MibTableColumn
rcExtLoopbackMode=_RcExtLoopbackMode_Object((1,3,6,1,4,1,8886,6,1,45,2,1,1,7),_RcExtLoopbackMode_Type())
rcExtLoopbackMode.setMaxAccess(_B)
if mibBuilder.loadTexts:rcExtLoopbackMode.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'RcExtLoopbackMode':RcExtLoopbackMode,'rcExtLoopback':rcExtLoopback,'rcExtloopbackObjectsGroup':rcExtloopbackObjectsGroup,'rcExtLoopbackBMDMacTransEnable':rcExtLoopbackBMDMacTransEnable,'rcExtloopbackConfigGroup':rcExtloopbackConfigGroup,'rcExtLoopbackTable':rcExtLoopbackTable,'rcExtLoopbackEntry':rcExtLoopbackEntry,_H:rcExtLoopbackPortIndex,'rcExtLoopbackDMac':rcExtLoopbackDMac,'rcExtLoopbackSMac':rcExtLoopbackSMac,'rcExtLoopbackSVlan':rcExtLoopbackSVlan,'rcExtLoopbackCVlan':rcExtLoopbackCVlan,'rcExtLoopbackTime':rcExtLoopbackTime,'rcExtLoopbackMode':rcExtLoopbackMode})