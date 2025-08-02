_F='eltPnacAuthSessionEntry'
_E='eltMesIssDot1xAuthConfigEntry'
_D='Integer32'
_C='ELTEX-MES-ISS-PNAC-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsPnacAuthSessionEntry,=mibBuilder.importSymbols('ARICENT-PNAC-MIB','fsPnacAuthSessionEntry')
eltMesIss,=mibBuilder.importSymbols('ELTEX-MES-ISS-MIB','eltMesIss')
dot1xAuthConfigEntry,=mibBuilder.importSymbols('IEEE8021-PAE-MIB','dot1xAuthConfigEntry')
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
eltMesIssPnacMIB=ModuleIdentity((1,3,6,1,4,1,35265,1,139,31))
if mibBuilder.loadTexts:eltMesIssPnacMIB.setRevisions(('2022-08-29 00:00','2022-06-20 00:00','2022-05-04 00:00'))
_EltMesIssPnacObjects_ObjectIdentity=ObjectIdentity
eltMesIssPnacObjects=_EltMesIssPnacObjects_ObjectIdentity((1,3,6,1,4,1,35265,1,139,31,1))
_EltMesIssDot1xGlobals_ObjectIdentity=ObjectIdentity
eltMesIssDot1xGlobals=_EltMesIssDot1xGlobals_ObjectIdentity((1,3,6,1,4,1,35265,1,139,31,1,1))
_EltMesIssDot1xPortConfig_ObjectIdentity=ObjectIdentity
eltMesIssDot1xPortConfig=_EltMesIssDot1xPortConfig_ObjectIdentity((1,3,6,1,4,1,35265,1,139,31,1,2))
_EltMesIssDot1xAuthConfigTable_Object=MibTable
eltMesIssDot1xAuthConfigTable=_EltMesIssDot1xAuthConfigTable_Object((1,3,6,1,4,1,35265,1,139,31,1,2,1))
if mibBuilder.loadTexts:eltMesIssDot1xAuthConfigTable.setStatus(_A)
_EltMesIssDot1xAuthConfigEntry_Object=MibTableRow
eltMesIssDot1xAuthConfigEntry=_EltMesIssDot1xAuthConfigEntry_Object((1,3,6,1,4,1,35265,1,139,31,1,2,1,1))
if mibBuilder.loadTexts:eltMesIssDot1xAuthConfigEntry.setStatus(_A)
_EltMesIssDot1xGuestVlanId_Type=VlanId
_EltMesIssDot1xGuestVlanId_Object=MibTableColumn
eltMesIssDot1xGuestVlanId=_EltMesIssDot1xGuestVlanId_Object((1,3,6,1,4,1,35265,1,139,31,1,2,1,1,1),_EltMesIssDot1xGuestVlanId_Type())
eltMesIssDot1xGuestVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDot1xGuestVlanId.setStatus(_A)
_EltMesIssDot1xUnauthenticatedVlanId_Type=VlanId
_EltMesIssDot1xUnauthenticatedVlanId_Object=MibTableColumn
eltMesIssDot1xUnauthenticatedVlanId=_EltMesIssDot1xUnauthenticatedVlanId_Object((1,3,6,1,4,1,35265,1,139,31,1,2,1,1,2),_EltMesIssDot1xUnauthenticatedVlanId_Type())
eltMesIssDot1xUnauthenticatedVlanId.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDot1xUnauthenticatedVlanId.setStatus(_A)
class _EltMesIssDot1xRadiusAttrVlanIdAction_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('ignore',1),('mandatory',2),('optional',3)))
_EltMesIssDot1xRadiusAttrVlanIdAction_Type.__name__=_D
_EltMesIssDot1xRadiusAttrVlanIdAction_Object=MibTableColumn
eltMesIssDot1xRadiusAttrVlanIdAction=_EltMesIssDot1xRadiusAttrVlanIdAction_Object((1,3,6,1,4,1,35265,1,139,31,1,2,1,1,3),_EltMesIssDot1xRadiusAttrVlanIdAction_Type())
eltMesIssDot1xRadiusAttrVlanIdAction.setMaxAccess(_B)
if mibBuilder.loadTexts:eltMesIssDot1xRadiusAttrVlanIdAction.setStatus(_A)
_EltMesIssDot1xAuthSession_ObjectIdentity=ObjectIdentity
eltMesIssDot1xAuthSession=_EltMesIssDot1xAuthSession_ObjectIdentity((1,3,6,1,4,1,35265,1,139,31,1,3))
_EltPnacAuthSessionTable_Object=MibTable
eltPnacAuthSessionTable=_EltPnacAuthSessionTable_Object((1,3,6,1,4,1,35265,1,139,31,1,3,1))
if mibBuilder.loadTexts:eltPnacAuthSessionTable.setStatus(_A)
_EltPnacAuthSessionEntry_Object=MibTableRow
eltPnacAuthSessionEntry=_EltPnacAuthSessionEntry_Object((1,3,6,1,4,1,35265,1,139,31,1,3,1,1))
if mibBuilder.loadTexts:eltPnacAuthSessionEntry.setStatus(_A)
_EltPnacAuthSessionCurrentVlanId_Type=VlanId
_EltPnacAuthSessionCurrentVlanId_Object=MibTableColumn
eltPnacAuthSessionCurrentVlanId=_EltPnacAuthSessionCurrentVlanId_Object((1,3,6,1,4,1,35265,1,139,31,1,3,1,1,1),_EltPnacAuthSessionCurrentVlanId_Type())
eltPnacAuthSessionCurrentVlanId.setMaxAccess('read-only')
if mibBuilder.loadTexts:eltPnacAuthSessionCurrentVlanId.setStatus(_A)
dot1xAuthConfigEntry.registerAugmentions((_C,_E))
eltMesIssDot1xAuthConfigEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())
fsPnacAuthSessionEntry.registerAugmentions((_C,_F))
eltPnacAuthSessionEntry.setIndexNames(*fsPnacAuthSessionEntry.getIndexNames())
mibBuilder.exportSymbols(_C,**{'eltMesIssPnacMIB':eltMesIssPnacMIB,'eltMesIssPnacObjects':eltMesIssPnacObjects,'eltMesIssDot1xGlobals':eltMesIssDot1xGlobals,'eltMesIssDot1xPortConfig':eltMesIssDot1xPortConfig,'eltMesIssDot1xAuthConfigTable':eltMesIssDot1xAuthConfigTable,_E:eltMesIssDot1xAuthConfigEntry,'eltMesIssDot1xGuestVlanId':eltMesIssDot1xGuestVlanId,'eltMesIssDot1xUnauthenticatedVlanId':eltMesIssDot1xUnauthenticatedVlanId,'eltMesIssDot1xRadiusAttrVlanIdAction':eltMesIssDot1xRadiusAttrVlanIdAction,'eltMesIssDot1xAuthSession':eltMesIssDot1xAuthSession,'eltPnacAuthSessionTable':eltPnacAuthSessionTable,_F:eltPnacAuthSessionEntry,'eltPnacAuthSessionCurrentVlanId':eltPnacAuthSessionCurrentVlanId})