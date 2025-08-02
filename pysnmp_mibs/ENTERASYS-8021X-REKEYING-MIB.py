_O='etsysDot1xRekeyingPairwiseGroup'
_N='etsysDot1xRekeyingBaseGroup'
_M='etsysDot1xRekeyPairwise'
_L='etsysDot1xRekeyAsymmetric'
_K='etsysDot1xRekeyLength'
_J='etsysDot1xRekeyEnabled'
_I='etsysDot1xRekeyPeriod'
_H='Unsigned32'
_G='Integer32'
_F='dot1xPaePortNumber'
_E='IEEE8021-PAE-MIB'
_D='TruthValue'
_C='read-write'
_B='ENTERASYS-8021X-REKEYING-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
etsysModules,=mibBuilder.importSymbols('ENTERASYS-MIB-NAMES','etsysModules')
dot1xPaePortNumber,=mibBuilder.importSymbols(_E,_F)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_G,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_H,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_D)
etsys8021xRekeyingMIB=ModuleIdentity((1,3,6,1,4,1,5624,1,2,17))
if mibBuilder.loadTexts:etsys8021xRekeyingMIB.setRevisions(('2004-07-14 15:07','2002-03-07 20:06'))
_EtsysDot1xRekeyingObjects_ObjectIdentity=ObjectIdentity
etsysDot1xRekeyingObjects=_EtsysDot1xRekeyingObjects_ObjectIdentity((1,3,6,1,4,1,5624,1,2,17,1))
_EtsysDot1xRekeyBaseBranch_ObjectIdentity=ObjectIdentity
etsysDot1xRekeyBaseBranch=_EtsysDot1xRekeyBaseBranch_ObjectIdentity((1,3,6,1,4,1,5624,1,2,17,1,1))
_EtsysDot1xRekeyConfigTable_Object=MibTable
etsysDot1xRekeyConfigTable=_EtsysDot1xRekeyConfigTable_Object((1,3,6,1,4,1,5624,1,2,17,1,1,1))
if mibBuilder.loadTexts:etsysDot1xRekeyConfigTable.setStatus(_A)
_EtsysDot1xRekeyConfigEntry_Object=MibTableRow
etsysDot1xRekeyConfigEntry=_EtsysDot1xRekeyConfigEntry_Object((1,3,6,1,4,1,5624,1,2,17,1,1,1,1))
etsysDot1xRekeyConfigEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:etsysDot1xRekeyConfigEntry.setStatus(_A)
class _EtsysDot1xRekeyEnabled_Type(TruthValue):defaultValue=2
_EtsysDot1xRekeyEnabled_Type.__name__=_D
_EtsysDot1xRekeyEnabled_Object=MibTableColumn
etsysDot1xRekeyEnabled=_EtsysDot1xRekeyEnabled_Object((1,3,6,1,4,1,5624,1,2,17,1,1,1,1,1),_EtsysDot1xRekeyEnabled_Type())
etsysDot1xRekeyEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xRekeyEnabled.setStatus(_A)
class _EtsysDot1xRekeyPeriod_Type(Unsigned32):defaultValue=1800
_EtsysDot1xRekeyPeriod_Type.__name__=_H
_EtsysDot1xRekeyPeriod_Object=MibTableColumn
etsysDot1xRekeyPeriod=_EtsysDot1xRekeyPeriod_Object((1,3,6,1,4,1,5624,1,2,17,1,1,1,1,2),_EtsysDot1xRekeyPeriod_Type())
etsysDot1xRekeyPeriod.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xRekeyPeriod.setStatus(_A)
class _EtsysDot1xRekeyLength_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('keylen40',1),('keylen128',2)))
_EtsysDot1xRekeyLength_Type.__name__=_G
_EtsysDot1xRekeyLength_Object=MibTableColumn
etsysDot1xRekeyLength=_EtsysDot1xRekeyLength_Object((1,3,6,1,4,1,5624,1,2,17,1,1,1,1,3),_EtsysDot1xRekeyLength_Type())
etsysDot1xRekeyLength.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xRekeyLength.setStatus(_A)
class _EtsysDot1xRekeyAsymmetric_Type(TruthValue):defaultValue=1
_EtsysDot1xRekeyAsymmetric_Type.__name__=_D
_EtsysDot1xRekeyAsymmetric_Object=MibTableColumn
etsysDot1xRekeyAsymmetric=_EtsysDot1xRekeyAsymmetric_Object((1,3,6,1,4,1,5624,1,2,17,1,1,1,1,4),_EtsysDot1xRekeyAsymmetric_Type())
etsysDot1xRekeyAsymmetric.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xRekeyAsymmetric.setStatus(_A)
class _EtsysDot1xRekeyPairwise_Type(TruthValue):defaultValue=1
_EtsysDot1xRekeyPairwise_Type.__name__=_D
_EtsysDot1xRekeyPairwise_Object=MibTableColumn
etsysDot1xRekeyPairwise=_EtsysDot1xRekeyPairwise_Object((1,3,6,1,4,1,5624,1,2,17,1,1,1,1,5),_EtsysDot1xRekeyPairwise_Type())
etsysDot1xRekeyPairwise.setMaxAccess(_C)
if mibBuilder.loadTexts:etsysDot1xRekeyPairwise.setStatus(_A)
_EtsysDot1xRekeyingConformance_ObjectIdentity=ObjectIdentity
etsysDot1xRekeyingConformance=_EtsysDot1xRekeyingConformance_ObjectIdentity((1,3,6,1,4,1,5624,1,2,17,2))
_EtsysDot1xRekeyingGroups_ObjectIdentity=ObjectIdentity
etsysDot1xRekeyingGroups=_EtsysDot1xRekeyingGroups_ObjectIdentity((1,3,6,1,4,1,5624,1,2,17,2,1))
_EtsysDot1xRekeyingCompliances_ObjectIdentity=ObjectIdentity
etsysDot1xRekeyingCompliances=_EtsysDot1xRekeyingCompliances_ObjectIdentity((1,3,6,1,4,1,5624,1,2,17,2,2))
etsysDot1xRekeyingBaseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,17,2,1,1))
etsysDot1xRekeyingBaseGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L)))
if mibBuilder.loadTexts:etsysDot1xRekeyingBaseGroup.setStatus(_A)
etsysDot1xRekeyingPairwiseGroup=ObjectGroup((1,3,6,1,4,1,5624,1,2,17,2,1,2))
etsysDot1xRekeyingPairwiseGroup.setObjects((_B,_M))
if mibBuilder.loadTexts:etsysDot1xRekeyingPairwiseGroup.setStatus(_A)
etsysDot1xRekeyingCompliance=ModuleCompliance((1,3,6,1,4,1,5624,1,2,17,2,2,1))
etsysDot1xRekeyingCompliance.setObjects(*((_B,_N),(_B,_O)))
if mibBuilder.loadTexts:etsysDot1xRekeyingCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'etsys8021xRekeyingMIB':etsys8021xRekeyingMIB,'etsysDot1xRekeyingObjects':etsysDot1xRekeyingObjects,'etsysDot1xRekeyBaseBranch':etsysDot1xRekeyBaseBranch,'etsysDot1xRekeyConfigTable':etsysDot1xRekeyConfigTable,'etsysDot1xRekeyConfigEntry':etsysDot1xRekeyConfigEntry,_J:etsysDot1xRekeyEnabled,_I:etsysDot1xRekeyPeriod,_K:etsysDot1xRekeyLength,_L:etsysDot1xRekeyAsymmetric,_M:etsysDot1xRekeyPairwise,'etsysDot1xRekeyingConformance':etsysDot1xRekeyingConformance,'etsysDot1xRekeyingGroups':etsysDot1xRekeyingGroups,_N:etsysDot1xRekeyingBaseGroup,_O:etsysDot1xRekeyingPairwiseGroup,'etsysDot1xRekeyingCompliances':etsysDot1xRekeyingCompliances,'etsysDot1xRekeyingCompliance':etsysDot1xRekeyingCompliance})