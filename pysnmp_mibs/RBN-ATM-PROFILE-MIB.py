_L='rbnAtmProfileGroup'
_K='rbnAtmTransmitBuffers'
_J='rbnAtmCellLossPriority'
_I='rbnAtmCountersEnabled'
_H='rbnAtmProfileName'
_G='rbnAtmProfileEntry'
_F='AtmProfileName'
_E='TruthValue'
_D='Integer32'
_C='read-create'
_B='RBN-ATM-PROFILE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
atmTrafficDescrParamEntry,=mibBuilder.importSymbols('ATM-MIB','atmTrafficDescrParamEntry')
rbnMgmt,=mibBuilder.importSymbols('RBN-SMI','rbnMgmt')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_E)
rbnAtmProfileMIB=ModuleIdentity((1,3,6,1,4,1,2352,2,2))
if mibBuilder.loadTexts:rbnAtmProfileMIB.setRevisions(('2002-04-19 00:00','2001-12-11 00:00','1998-07-15 16:45'))
class AtmProfileName(TextualConvention,OctetString):status=_A;displayHint='80a';subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,80))
_RbnAtmProfileMIBObjects_ObjectIdentity=ObjectIdentity
rbnAtmProfileMIBObjects=_RbnAtmProfileMIBObjects_ObjectIdentity((1,3,6,1,4,1,2352,2,2,1))
_RbnAtmProfileTable_Object=MibTable
rbnAtmProfileTable=_RbnAtmProfileTable_Object((1,3,6,1,4,1,2352,2,2,1,1))
if mibBuilder.loadTexts:rbnAtmProfileTable.setStatus(_A)
_RbnAtmProfileEntry_Object=MibTableRow
rbnAtmProfileEntry=_RbnAtmProfileEntry_Object((1,3,6,1,4,1,2352,2,2,1,1,1))
if mibBuilder.loadTexts:rbnAtmProfileEntry.setStatus(_A)
class _RbnAtmProfileName_Type(AtmProfileName):defaultHexValue=''
_RbnAtmProfileName_Type.__name__=_F
_RbnAtmProfileName_Object=MibTableColumn
rbnAtmProfileName=_RbnAtmProfileName_Object((1,3,6,1,4,1,2352,2,2,1,1,1,1),_RbnAtmProfileName_Type())
rbnAtmProfileName.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmProfileName.setStatus(_A)
class _RbnAtmCountersEnabled_Type(TruthValue):defaultValue=2
_RbnAtmCountersEnabled_Type.__name__=_E
_RbnAtmCountersEnabled_Object=MibTableColumn
rbnAtmCountersEnabled=_RbnAtmCountersEnabled_Object((1,3,6,1,4,1,2352,2,2,1,1,1,2),_RbnAtmCountersEnabled_Type())
rbnAtmCountersEnabled.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmCountersEnabled.setStatus(_A)
_RbnAtmCellLossPriority_Type=TruthValue
_RbnAtmCellLossPriority_Object=MibTableColumn
rbnAtmCellLossPriority=_RbnAtmCellLossPriority_Object((1,3,6,1,4,1,2352,2,2,1,1,1,3),_RbnAtmCellLossPriority_Type())
rbnAtmCellLossPriority.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmCellLossPriority.setStatus(_A)
class _RbnAtmTransmitBuffers_Type(Integer32):defaultValue=50;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,63))
_RbnAtmTransmitBuffers_Type.__name__=_D
_RbnAtmTransmitBuffers_Object=MibTableColumn
rbnAtmTransmitBuffers=_RbnAtmTransmitBuffers_Object((1,3,6,1,4,1,2352,2,2,1,1,1,4),_RbnAtmTransmitBuffers_Type())
rbnAtmTransmitBuffers.setMaxAccess(_C)
if mibBuilder.loadTexts:rbnAtmTransmitBuffers.setStatus(_A)
_RbnAtmProfileMIBConformance_ObjectIdentity=ObjectIdentity
rbnAtmProfileMIBConformance=_RbnAtmProfileMIBConformance_ObjectIdentity((1,3,6,1,4,1,2352,2,2,2))
_RbnAtmProfileMIBGroups_ObjectIdentity=ObjectIdentity
rbnAtmProfileMIBGroups=_RbnAtmProfileMIBGroups_ObjectIdentity((1,3,6,1,4,1,2352,2,2,2,1))
_RbnAtmProfileMIBCompliances_ObjectIdentity=ObjectIdentity
rbnAtmProfileMIBCompliances=_RbnAtmProfileMIBCompliances_ObjectIdentity((1,3,6,1,4,1,2352,2,2,2,2))
atmTrafficDescrParamEntry.registerAugmentions((_B,_G))
rbnAtmProfileEntry.setIndexNames(*atmTrafficDescrParamEntry.getIndexNames())
rbnAtmProfileGroup=ObjectGroup((1,3,6,1,4,1,2352,2,2,2,1,1))
rbnAtmProfileGroup.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K)))
if mibBuilder.loadTexts:rbnAtmProfileGroup.setStatus(_A)
rbnAtmProfileMIBCompliance=ModuleCompliance((1,3,6,1,4,1,2352,2,2,2,2,1))
rbnAtmProfileMIBCompliance.setObjects((_B,_L))
if mibBuilder.loadTexts:rbnAtmProfileMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{_F:AtmProfileName,'rbnAtmProfileMIB':rbnAtmProfileMIB,'rbnAtmProfileMIBObjects':rbnAtmProfileMIBObjects,'rbnAtmProfileTable':rbnAtmProfileTable,_G:rbnAtmProfileEntry,_H:rbnAtmProfileName,_I:rbnAtmCountersEnabled,_J:rbnAtmCellLossPriority,_K:rbnAtmTransmitBuffers,'rbnAtmProfileMIBConformance':rbnAtmProfileMIBConformance,'rbnAtmProfileMIBGroups':rbnAtmProfileMIBGroups,_L:rbnAtmProfileGroup,'rbnAtmProfileMIBCompliances':rbnAtmProfileMIBCompliances,'rbnAtmProfileMIBCompliance':rbnAtmProfileMIBCompliance})