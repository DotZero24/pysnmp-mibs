_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
adGenTa5kCommonDs1Prov,adGenTa5kCommonDs1ProvID=mibBuilder.importSymbols('ADTRAN-GENTA5K-MIB','adGenTa5kCommonDs1Prov','adGenTa5kCommonDs1ProvID')
ifIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
adGenCommonDs1ProvMIB=ModuleIdentity((1,3,6,1,4,1,664,6,10000,67,1,6,1))
_AdDs1vgDs1Mgmt_ObjectIdentity=ObjectIdentity
adDs1vgDs1Mgmt=_AdDs1vgDs1Mgmt_ObjectIdentity((1,3,6,1,4,1,664,5,67,1,6,1))
_AdDs1vgT1InterfaceProvisioningTable_Object=MibTable
adDs1vgT1InterfaceProvisioningTable=_AdDs1vgT1InterfaceProvisioningTable_Object((1,3,6,1,4,1,664,5,67,1,6,1,1))
if mibBuilder.loadTexts:adDs1vgT1InterfaceProvisioningTable.setStatus(_A)
_AdDs1vgT1InterfaceProvisioningTableEntry_Object=MibTableRow
adDs1vgT1InterfaceProvisioningTableEntry=_AdDs1vgT1InterfaceProvisioningTableEntry_Object((1,3,6,1,4,1,664,5,67,1,6,1,1,1))
adDs1vgT1InterfaceProvisioningTableEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:adDs1vgT1InterfaceProvisioningTableEntry.setStatus(_A)
class _AdDs1vgT1InterfaceProvTableLineBuildout_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('lineLength0ft',1),('lineLength0133ft',2),('lineLength133266ft',3),('lineLength266399ft',4),('lineLength399533ft',5),('lineLength533655ft',6)))
_AdDs1vgT1InterfaceProvTableLineBuildout_Type.__name__=_B
_AdDs1vgT1InterfaceProvTableLineBuildout_Object=MibTableColumn
adDs1vgT1InterfaceProvTableLineBuildout=_AdDs1vgT1InterfaceProvTableLineBuildout_Object((1,3,6,1,4,1,664,5,67,1,6,1,1,1,1),_AdDs1vgT1InterfaceProvTableLineBuildout_Type())
adDs1vgT1InterfaceProvTableLineBuildout.setMaxAccess(_C)
if mibBuilder.loadTexts:adDs1vgT1InterfaceProvTableLineBuildout.setStatus(_A)
class _AdDs1vgT1InterfaceProvTableLineMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('gr303cesop',1),('satop',2)))
_AdDs1vgT1InterfaceProvTableLineMode_Type.__name__=_B
_AdDs1vgT1InterfaceProvTableLineMode_Object=MibTableColumn
adDs1vgT1InterfaceProvTableLineMode=_AdDs1vgT1InterfaceProvTableLineMode_Object((1,3,6,1,4,1,664,5,67,1,6,1,1,1,2),_AdDs1vgT1InterfaceProvTableLineMode_Type())
adDs1vgT1InterfaceProvTableLineMode.setMaxAccess(_C)
if mibBuilder.loadTexts:adDs1vgT1InterfaceProvTableLineMode.setStatus(_A)
class _AdDs1vgT1InterfaceClearPMCounters_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_AdDs1vgT1InterfaceClearPMCounters_Type.__name__=_B
_AdDs1vgT1InterfaceClearPMCounters_Object=MibTableColumn
adDs1vgT1InterfaceClearPMCounters=_AdDs1vgT1InterfaceClearPMCounters_Object((1,3,6,1,4,1,664,5,67,1,6,1,1,1,3),_AdDs1vgT1InterfaceClearPMCounters_Type())
adDs1vgT1InterfaceClearPMCounters.setMaxAccess(_C)
if mibBuilder.loadTexts:adDs1vgT1InterfaceClearPMCounters.setStatus(_A)
mibBuilder.exportSymbols('ADTRAN-COMMON-DS1PROV-MIB',**{'adDs1vgDs1Mgmt':adDs1vgDs1Mgmt,'adDs1vgT1InterfaceProvisioningTable':adDs1vgT1InterfaceProvisioningTable,'adDs1vgT1InterfaceProvisioningTableEntry':adDs1vgT1InterfaceProvisioningTableEntry,'adDs1vgT1InterfaceProvTableLineBuildout':adDs1vgT1InterfaceProvTableLineBuildout,'adDs1vgT1InterfaceProvTableLineMode':adDs1vgT1InterfaceProvTableLineMode,'adDs1vgT1InterfaceClearPMCounters':adDs1vgT1InterfaceClearPMCounters,'adGenCommonDs1ProvMIB':adGenCommonDs1ProvMIB})