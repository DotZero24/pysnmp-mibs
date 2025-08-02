_P='h323AliasesGroupAliasesGroupVer1'
_O='h323AliasesLineAliasesGroupVer1'
_N='h323GroupAliasesCurrent'
_M='h323GroupAliasesConfigured'
_L='h323AliasesCurrent'
_K='h323AliasesConfigured'
_J='read-write'
_I='Unsigned32'
_H='groupIndex'
_G='MX-LINE-GROUPING-MIB'
_F='ifIndex'
_E='IF-MIB'
_D='read-only'
_C='OctetString'
_B='MX-H323-ALIASES-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,=mibBuilder.importSymbols(_E,_F)
h323,=mibBuilder.importSymbols('MX-H323-MIB','h323')
groupIndex,=mibBuilder.importSymbols(_G,_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_I,'iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
h323AliasesMIB=ModuleIdentity((1,3,6,1,4,1,4935,20,30,15))
if mibBuilder.loadTexts:h323AliasesMIB.setRevisions(('1903-03-03 00:00',))
_H323AliasesMIBObjects_ObjectIdentity=ObjectIdentity
h323AliasesMIBObjects=_H323AliasesMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,20,30,15,1))
_H323AliasesIfAliasesTable_Object=MibTable
h323AliasesIfAliasesTable=_H323AliasesIfAliasesTable_Object((1,3,6,1,4,1,4935,20,30,15,1,5))
if mibBuilder.loadTexts:h323AliasesIfAliasesTable.setStatus(_A)
_H323AliasesIfAliasesEntry_Object=MibTableRow
h323AliasesIfAliasesEntry=_H323AliasesIfAliasesEntry_Object((1,3,6,1,4,1,4935,20,30,15,1,5,1))
h323AliasesIfAliasesEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:h323AliasesIfAliasesEntry.setStatus(_A)
class _H323AliasesGroupIndex_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,24))
_H323AliasesGroupIndex_Type.__name__=_I
_H323AliasesGroupIndex_Object=MibTableColumn
h323AliasesGroupIndex=_H323AliasesGroupIndex_Object((1,3,6,1,4,1,4935,20,30,15,1,5,1,5),_H323AliasesGroupIndex_Type())
h323AliasesGroupIndex.setMaxAccess(_D)
if mibBuilder.loadTexts:h323AliasesGroupIndex.setStatus(_A)
class _H323AliasesConfigured_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H323AliasesConfigured_Type.__name__=_C
_H323AliasesConfigured_Object=MibTableColumn
h323AliasesConfigured=_H323AliasesConfigured_Object((1,3,6,1,4,1,4935,20,30,15,1,5,1,10),_H323AliasesConfigured_Type())
h323AliasesConfigured.setMaxAccess(_J)
if mibBuilder.loadTexts:h323AliasesConfigured.setStatus(_A)
class _H323AliasesCurrent_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H323AliasesCurrent_Type.__name__=_C
_H323AliasesCurrent_Object=MibTableColumn
h323AliasesCurrent=_H323AliasesCurrent_Object((1,3,6,1,4,1,4935,20,30,15,1,5,1,15),_H323AliasesCurrent_Type())
h323AliasesCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:h323AliasesCurrent.setStatus(_A)
_H323AliasesGroupAliasesTable_Object=MibTable
h323AliasesGroupAliasesTable=_H323AliasesGroupAliasesTable_Object((1,3,6,1,4,1,4935,20,30,15,1,10))
if mibBuilder.loadTexts:h323AliasesGroupAliasesTable.setStatus(_A)
_H323AliasesGroupAliasesEntry_Object=MibTableRow
h323AliasesGroupAliasesEntry=_H323AliasesGroupAliasesEntry_Object((1,3,6,1,4,1,4935,20,30,15,1,10,1))
h323AliasesGroupAliasesEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:h323AliasesGroupAliasesEntry.setStatus(_A)
class _H323GroupAliasesConfigured_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_H323GroupAliasesConfigured_Type.__name__=_C
_H323GroupAliasesConfigured_Object=MibTableColumn
h323GroupAliasesConfigured=_H323GroupAliasesConfigured_Object((1,3,6,1,4,1,4935,20,30,15,1,10,1,5),_H323GroupAliasesConfigured_Type())
h323GroupAliasesConfigured.setMaxAccess(_J)
if mibBuilder.loadTexts:h323GroupAliasesConfigured.setStatus(_A)
class _H323GroupAliasesCurrent_Type(OctetString):defaultValue=OctetString('');subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_H323GroupAliasesCurrent_Type.__name__=_C
_H323GroupAliasesCurrent_Object=MibTableColumn
h323GroupAliasesCurrent=_H323GroupAliasesCurrent_Object((1,3,6,1,4,1,4935,20,30,15,1,10,1,10),_H323GroupAliasesCurrent_Type())
h323GroupAliasesCurrent.setMaxAccess(_D)
if mibBuilder.loadTexts:h323GroupAliasesCurrent.setStatus(_A)
_H323AliasesConformance_ObjectIdentity=ObjectIdentity
h323AliasesConformance=_H323AliasesConformance_ObjectIdentity((1,3,6,1,4,1,4935,20,30,15,2))
_H323AliasesCompliances_ObjectIdentity=ObjectIdentity
h323AliasesCompliances=_H323AliasesCompliances_ObjectIdentity((1,3,6,1,4,1,4935,20,30,15,2,1))
_H323AliasesGroups_ObjectIdentity=ObjectIdentity
h323AliasesGroups=_H323AliasesGroups_ObjectIdentity((1,3,6,1,4,1,4935,20,30,15,2,2))
h323AliasesLineAliasesGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,15,2,2,5))
h323AliasesLineAliasesGroupVer1.setObjects(*((_B,_K),(_B,_L)))
if mibBuilder.loadTexts:h323AliasesLineAliasesGroupVer1.setStatus(_A)
h323AliasesGroupAliasesGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,20,30,15,2,2,10))
h323AliasesGroupAliasesGroupVer1.setObjects(*((_B,_M),(_B,_N)))
if mibBuilder.loadTexts:h323AliasesGroupAliasesGroupVer1.setStatus(_A)
h323AliasesBasicComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,20,30,15,2,1,5))
h323AliasesBasicComplVer1.setObjects(*((_B,_O),(_B,_P)))
if mibBuilder.loadTexts:h323AliasesBasicComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'h323AliasesMIB':h323AliasesMIB,'h323AliasesMIBObjects':h323AliasesMIBObjects,'h323AliasesIfAliasesTable':h323AliasesIfAliasesTable,'h323AliasesIfAliasesEntry':h323AliasesIfAliasesEntry,'h323AliasesGroupIndex':h323AliasesGroupIndex,_K:h323AliasesConfigured,_L:h323AliasesCurrent,'h323AliasesGroupAliasesTable':h323AliasesGroupAliasesTable,'h323AliasesGroupAliasesEntry':h323AliasesGroupAliasesEntry,_M:h323GroupAliasesConfigured,_N:h323GroupAliasesCurrent,'h323AliasesConformance':h323AliasesConformance,'h323AliasesCompliances':h323AliasesCompliances,'h323AliasesBasicComplVer1':h323AliasesBasicComplVer1,'h323AliasesGroups':h323AliasesGroups,_O:h323AliasesLineAliasesGroupVer1,_P:h323AliasesGroupAliasesGroupVer1})