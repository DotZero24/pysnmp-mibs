_H='eltMesIssMstMstiPortEntry'
_G='eltMesIssMstInstanceId'
_F='read-write'
_E='ELTEX-MES-ISS-MST-MIB'
_D='Integer32'
_C='read-only'
_B='OctetString'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_B,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMstMstiPortEntry,=mibBuilder.importSymbols('ARICENT-MST-MIB','fsMstMstiPortEntry')
eltMesIssBridgeMIBObjects,=mibBuilder.importSymbols('ELTEX-MES-ISS-BRIDGE-MIB','eltMesIssBridgeMIBObjects')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
eltMesIssMstMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,14,1,1))
if mibBuilder.loadTexts:eltMesIssMstMIB.setRevisions(('2020-09-22 00:00','2019-06-03 00:00'))
class EltMesIssMstPendingConfigAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('commit',1),('revert',2)))
_EltMesIssMstMIBObjects_ObjectIdentity=ObjectIdentity
eltMesIssMstMIBObjects=_EltMesIssMstMIBObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,14,1,1,1))
_EltMesIssMstGlobals_ObjectIdentity=ObjectIdentity
eltMesIssMstGlobals=_EltMesIssMstGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,14,1,1,1,1))
_EltMesIssMstConfigPending_ObjectIdentity=ObjectIdentity
eltMesIssMstConfigPending=_EltMesIssMstConfigPending_ObjectIdentity((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1))
_EltMesIssMstPendingConfigAction_Type=EltMesIssMstPendingConfigAction
_EltMesIssMstPendingConfigAction_Object=MibScalar
eltMesIssMstPendingConfigAction=_EltMesIssMstPendingConfigAction_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,1),_EltMesIssMstPendingConfigAction_Type())
eltMesIssMstPendingConfigAction.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssMstPendingConfigAction.setStatus(_A)
class _EltMesIssMstRegnNamePending_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_EltMesIssMstRegnNamePending_Type.__name__=_B
_EltMesIssMstRegnNamePending_Object=MibScalar
eltMesIssMstRegnNamePending=_EltMesIssMstRegnNamePending_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,2),_EltMesIssMstRegnNamePending_Type())
eltMesIssMstRegnNamePending.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssMstRegnNamePending.setStatus(_A)
class _EltMesIssMstRegnVersionPending_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_EltMesIssMstRegnVersionPending_Type.__name__=_D
_EltMesIssMstRegnVersionPending_Object=MibScalar
eltMesIssMstRegnVersionPending=_EltMesIssMstRegnVersionPending_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,3),_EltMesIssMstRegnVersionPending_Type())
eltMesIssMstRegnVersionPending.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssMstRegnVersionPending.setStatus(_A)
_EltMesIssMstVlanMapPendingTable_Object=MibTable
eltMesIssMstVlanMapPendingTable=_EltMesIssMstVlanMapPendingTable_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,4))
if mibBuilder.loadTexts:eltMesIssMstVlanMapPendingTable.setStatus(_A)
_EltMesIssMstVlanMapPendingEntry_Object=MibTableRow
eltMesIssMstVlanMapPendingEntry=_EltMesIssMstVlanMapPendingEntry_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,4,1))
eltMesIssMstVlanMapPendingEntry.setIndexNames((0,_E,_G))
if mibBuilder.loadTexts:eltMesIssMstVlanMapPendingEntry.setStatus(_A)
class _EltMesIssMstInstanceId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64),ValueRangeConstraint(4094,4094))
_EltMesIssMstInstanceId_Type.__name__=_D
_EltMesIssMstInstanceId_Object=MibTableColumn
eltMesIssMstInstanceId=_EltMesIssMstInstanceId_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,4,1,1),_EltMesIssMstInstanceId_Type())
eltMesIssMstInstanceId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:eltMesIssMstInstanceId.setStatus(_A)
class _EltMesIssMstVlanMapPending_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesIssMstVlanMapPending_Type.__name__=_B
_EltMesIssMstVlanMapPending_Object=MibTableColumn
eltMesIssMstVlanMapPending=_EltMesIssMstVlanMapPending_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,4,1,2),_EltMesIssMstVlanMapPending_Type())
eltMesIssMstVlanMapPending.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssMstVlanMapPending.setStatus(_A)
class _EltMesIssMstVlanMap2kPending_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesIssMstVlanMap2kPending_Type.__name__=_B
_EltMesIssMstVlanMap2kPending_Object=MibTableColumn
eltMesIssMstVlanMap2kPending=_EltMesIssMstVlanMap2kPending_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,4,1,3),_EltMesIssMstVlanMap2kPending_Type())
eltMesIssMstVlanMap2kPending.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssMstVlanMap2kPending.setStatus(_A)
class _EltMesIssMstVlanMap3kPending_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesIssMstVlanMap3kPending_Type.__name__=_B
_EltMesIssMstVlanMap3kPending_Object=MibTableColumn
eltMesIssMstVlanMap3kPending=_EltMesIssMstVlanMap3kPending_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,4,1,4),_EltMesIssMstVlanMap3kPending_Type())
eltMesIssMstVlanMap3kPending.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssMstVlanMap3kPending.setStatus(_A)
class _EltMesIssMstVlanMap4kPending_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,128))
_EltMesIssMstVlanMap4kPending_Type.__name__=_B
_EltMesIssMstVlanMap4kPending_Object=MibTableColumn
eltMesIssMstVlanMap4kPending=_EltMesIssMstVlanMap4kPending_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,1,4,1,5),_EltMesIssMstVlanMap4kPending_Type())
eltMesIssMstVlanMap4kPending.setMaxAccess(_C)
if mibBuilder.loadTexts:eltMesIssMstVlanMap4kPending.setStatus(_A)
_EltMesIssMstMstiConfig_ObjectIdentity=ObjectIdentity
eltMesIssMstMstiConfig=_EltMesIssMstMstiConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,2))
_EltMesIssMstMstiPortTable_Object=MibTable
eltMesIssMstMstiPortTable=_EltMesIssMstMstiPortTable_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,2,1))
if mibBuilder.loadTexts:eltMesIssMstMstiPortTable.setStatus(_A)
_EltMesIssMstMstiPortEntry_Object=MibTableRow
eltMesIssMstMstiPortEntry=_EltMesIssMstMstiPortEntry_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,2,1,1))
if mibBuilder.loadTexts:eltMesIssMstMstiPortEntry.setStatus(_A)
_EltMesIssMstMstiRootGuard_Type=TruthValue
_EltMesIssMstMstiRootGuard_Object=MibTableColumn
eltMesIssMstMstiRootGuard=_EltMesIssMstMstiRootGuard_Object((1,3,6,1,4,1,35265,1,139,14,1,1,1,1,2,1,1,1),_EltMesIssMstMstiRootGuard_Type())
eltMesIssMstMstiRootGuard.setMaxAccess(_F)
if mibBuilder.loadTexts:eltMesIssMstMstiRootGuard.setStatus(_A)
fsMstMstiPortEntry.registerAugmentions((_E,_H))
eltMesIssMstMstiPortEntry.setIndexNames(*fsMstMstiPortEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'EltMesIssMstPendingConfigAction':EltMesIssMstPendingConfigAction,'eltMesIssMstMIB':eltMesIssMstMIB,'eltMesIssMstMIBObjects':eltMesIssMstMIBObjects,'eltMesIssMstGlobals':eltMesIssMstGlobals,'eltMesIssMstConfigPending':eltMesIssMstConfigPending,'eltMesIssMstPendingConfigAction':eltMesIssMstPendingConfigAction,'eltMesIssMstRegnNamePending':eltMesIssMstRegnNamePending,'eltMesIssMstRegnVersionPending':eltMesIssMstRegnVersionPending,'eltMesIssMstVlanMapPendingTable':eltMesIssMstVlanMapPendingTable,'eltMesIssMstVlanMapPendingEntry':eltMesIssMstVlanMapPendingEntry,_G:eltMesIssMstInstanceId,'eltMesIssMstVlanMapPending':eltMesIssMstVlanMapPending,'eltMesIssMstVlanMap2kPending':eltMesIssMstVlanMap2kPending,'eltMesIssMstVlanMap3kPending':eltMesIssMstVlanMap3kPending,'eltMesIssMstVlanMap4kPending':eltMesIssMstVlanMap4kPending,'eltMesIssMstMstiConfig':eltMesIssMstMstiConfig,'eltMesIssMstMstiPortTable':eltMesIssMstMstiPortTable,_H:eltMesIssMstMstiPortEntry,'eltMesIssMstMstiRootGuard':eltMesIssMstMstiRootGuard})