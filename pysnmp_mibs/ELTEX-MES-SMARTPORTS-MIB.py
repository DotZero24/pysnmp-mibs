_F='eltSmartPortsMacroManageEntry'
_E='ELTEX-MES-SMARTPORTS-MIB'
_D='read-write'
_C='Unsigned32'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltMes,=mibBuilder.importSymbols('ELTEX-MES','eltMes')
rlSmartPortsMacroManageEntry,=mibBuilder.importSymbols('RADLAN-SMARTPORTS-MIB','rlSmartPortsMacroManageEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_C,'iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
eltMesSmartPorts=ModuleIdentity((1,3,6,1,4,1,35265,1,23,17))
_EltMesSmartPortsObjects_ObjectIdentity=ObjectIdentity
eltMesSmartPortsObjects=_EltMesSmartPortsObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,23,17,1))
_EltMesSmartPortsGlobals_ObjectIdentity=ObjectIdentity
eltMesSmartPortsGlobals=_EltMesSmartPortsGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,23,17,1,1))
_EltMesSmartPortsConfigs_ObjectIdentity=ObjectIdentity
eltMesSmartPortsConfigs=_EltMesSmartPortsConfigs_ObjectIdentity((1,3,6,1,4,1,35265,1,23,17,1,2))
_EltSmartPortsMacroManageTable_Object=MibTable
eltSmartPortsMacroManageTable=_EltSmartPortsMacroManageTable_Object((1,3,6,1,4,1,35265,1,23,17,1,2,1))
if mibBuilder.loadTexts:eltSmartPortsMacroManageTable.setStatus(_A)
_EltSmartPortsMacroManageEntry_Object=MibTableRow
eltSmartPortsMacroManageEntry=_EltSmartPortsMacroManageEntry_Object((1,3,6,1,4,1,35265,1,23,17,1,2,1,1))
if mibBuilder.loadTexts:eltSmartPortsMacroManageEntry.setStatus(_A)
class _EltSmartPortsMacroTrackObject_Type(Unsigned32):defaultValue=0
_EltSmartPortsMacroTrackObject_Type.__name__=_C
_EltSmartPortsMacroTrackObject_Object=MibTableColumn
eltSmartPortsMacroTrackObject=_EltSmartPortsMacroTrackObject_Object((1,3,6,1,4,1,35265,1,23,17,1,2,1,1,1),_EltSmartPortsMacroTrackObject_Type())
eltSmartPortsMacroTrackObject.setMaxAccess(_D)
if mibBuilder.loadTexts:eltSmartPortsMacroTrackObject.setStatus(_A)
class _EltSmartPortsMacroTrackActivationState_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*(('any',0),('up',1),('down',2)))
_EltSmartPortsMacroTrackActivationState_Type.__name__=_B
_EltSmartPortsMacroTrackActivationState_Object=MibTableColumn
eltSmartPortsMacroTrackActivationState=_EltSmartPortsMacroTrackActivationState_Object((1,3,6,1,4,1,35265,1,23,17,1,2,1,1,2),_EltSmartPortsMacroTrackActivationState_Type())
eltSmartPortsMacroTrackActivationState.setMaxAccess(_D)
if mibBuilder.loadTexts:eltSmartPortsMacroTrackActivationState.setStatus(_A)
rlSmartPortsMacroManageEntry.registerAugmentions((_E,_F))
eltSmartPortsMacroManageEntry.setIndexNames(*rlSmartPortsMacroManageEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'eltMesSmartPorts':eltMesSmartPorts,'eltMesSmartPortsObjects':eltMesSmartPortsObjects,'eltMesSmartPortsGlobals':eltMesSmartPortsGlobals,'eltMesSmartPortsConfigs':eltMesSmartPortsConfigs,'eltSmartPortsMacroManageTable':eltSmartPortsMacroManageTable,_F:eltSmartPortsMacroManageEntry,'eltSmartPortsMacroTrackObject':eltSmartPortsMacroTrackObject,'eltSmartPortsMacroTrackActivationState':eltSmartPortsMacroTrackActivationState})