_H='not-accessible'
_G='eltexSqinqClassifierVlan'
_F='eltexSqinqDirection'
_E='ifIndex'
_D='IF-MIB'
_C='read-write'
_B='ELTEX-VLAN-TRANSLATION-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
eltexLtd,=mibBuilder.importSymbols('ELTEX-SMI-ACTUAL','eltexLtd')
ifIndex,=mibBuilder.importSymbols(_D,_E)
VlanId,=mibBuilder.importSymbols('Q-BRIDGE-MIB','VlanId')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
eltexVlanTranslationMIB=ModuleIdentity((1,3,6,1,4,1,35265,54))
if mibBuilder.loadTexts:eltexVlanTranslationMIB.setRevisions(('2019-11-07 00:00','2019-02-04 00:00'))
class EltexSqinqDirection(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
class EltexSqinqAction(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('overrideVlan',1),('addVlan',2),('permit',3),('deny',4)))
_EltexVlanTranslationObjects_ObjectIdentity=ObjectIdentity
eltexVlanTranslationObjects=_EltexVlanTranslationObjects_ObjectIdentity((1,3,6,1,4,1,35265,54,1))
_EltexSqinqObjects_ObjectIdentity=ObjectIdentity
eltexSqinqObjects=_EltexSqinqObjects_ObjectIdentity((1,3,6,1,4,1,35265,54,1,1))
_EltexSqinqGlobals_ObjectIdentity=ObjectIdentity
eltexSqinqGlobals=_EltexSqinqGlobals_ObjectIdentity((1,3,6,1,4,1,35265,54,1,1,1))
_EltexSqinqConfigs_ObjectIdentity=ObjectIdentity
eltexSqinqConfigs=_EltexSqinqConfigs_ObjectIdentity((1,3,6,1,4,1,35265,54,1,1,2))
_EltexSqinqPortTable_Object=MibTable
eltexSqinqPortTable=_EltexSqinqPortTable_Object((1,3,6,1,4,1,35265,54,1,1,2,1))
if mibBuilder.loadTexts:eltexSqinqPortTable.setStatus(_A)
_EltexSqinqPortEntry_Object=MibTableRow
eltexSqinqPortEntry=_EltexSqinqPortEntry_Object((1,3,6,1,4,1,35265,54,1,1,2,1,1))
eltexSqinqPortEntry.setIndexNames((0,_D,_E),(0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:eltexSqinqPortEntry.setStatus(_A)
_EltexSqinqDirection_Type=EltexSqinqDirection
_EltexSqinqDirection_Object=MibTableColumn
eltexSqinqDirection=_EltexSqinqDirection_Object((1,3,6,1,4,1,35265,54,1,1,2,1,1,1),_EltexSqinqDirection_Type())
eltexSqinqDirection.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexSqinqDirection.setStatus(_A)
_EltexSqinqClassifierVlan_Type=VlanId
_EltexSqinqClassifierVlan_Object=MibTableColumn
eltexSqinqClassifierVlan=_EltexSqinqClassifierVlan_Object((1,3,6,1,4,1,35265,54,1,1,2,1,1,2),_EltexSqinqClassifierVlan_Type())
eltexSqinqClassifierVlan.setMaxAccess(_H)
if mibBuilder.loadTexts:eltexSqinqClassifierVlan.setStatus(_A)
_EltexSqinqAction_Type=EltexSqinqAction
_EltexSqinqAction_Object=MibTableColumn
eltexSqinqAction=_EltexSqinqAction_Object((1,3,6,1,4,1,35265,54,1,1,2,1,1,3),_EltexSqinqAction_Type())
eltexSqinqAction.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexSqinqAction.setStatus(_A)
_EltexSqinqActionVlan_Type=VlanId
_EltexSqinqActionVlan_Object=MibTableColumn
eltexSqinqActionVlan=_EltexSqinqActionVlan_Object((1,3,6,1,4,1,35265,54,1,1,2,1,1,4),_EltexSqinqActionVlan_Type())
eltexSqinqActionVlan.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexSqinqActionVlan.setStatus(_A)
_EltexSqinqRowStatus_Type=RowStatus
_EltexSqinqRowStatus_Object=MibTableColumn
eltexSqinqRowStatus=_EltexSqinqRowStatus_Object((1,3,6,1,4,1,35265,54,1,1,2,1,1,5),_EltexSqinqRowStatus_Type())
eltexSqinqRowStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:eltexSqinqRowStatus.setStatus(_A)
_EltexSqinqStatistics_ObjectIdentity=ObjectIdentity
eltexSqinqStatistics=_EltexSqinqStatistics_ObjectIdentity((1,3,6,1,4,1,35265,54,1,1,3))
mibBuilder.exportSymbols(_B,**{'EltexSqinqDirection':EltexSqinqDirection,'EltexSqinqAction':EltexSqinqAction,'eltexVlanTranslationMIB':eltexVlanTranslationMIB,'eltexVlanTranslationObjects':eltexVlanTranslationObjects,'eltexSqinqObjects':eltexSqinqObjects,'eltexSqinqGlobals':eltexSqinqGlobals,'eltexSqinqConfigs':eltexSqinqConfigs,'eltexSqinqPortTable':eltexSqinqPortTable,'eltexSqinqPortEntry':eltexSqinqPortEntry,_F:eltexSqinqDirection,_G:eltexSqinqClassifierVlan,'eltexSqinqAction':eltexSqinqAction,'eltexSqinqActionVlan':eltexSqinqActionVlan,'eltexSqinqRowStatus':eltexSqinqRowStatus,'eltexSqinqStatistics':eltexSqinqStatistics})