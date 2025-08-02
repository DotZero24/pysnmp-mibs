_R='juniAutoConfGroup2'
_Q='juniAutoConfGroup'
_P='juniAutoConfNextLockoutTime'
_O='juniAutoConfLockoutElapsedTime'
_N='juniAutoConfLockoutTime'
_M='juniAutoConfLockoutMax'
_L='juniAutoConfLockoutMin'
_K='juniAutoConfLockoutSupported'
_J='obsolete'
_I='juniAutoConfEnable'
_H='not-accessible'
_G='juniAutoConfEncaps'
_F='juniAutoConfIfIndex'
_E='read-write'
_D='read-only'
_C='Integer32'
_B='Juniper-AUTOCONFIGURE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
juniMibs,=mibBuilder.importSymbols('Juniper-MIBs','juniMibs')
JuniEnable,=mibBuilder.importSymbols('Juniper-TC','JuniEnable')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
juniAutoConfMIB=ModuleIdentity((1,3,6,1,4,1,4874,2,2,48))
if mibBuilder.loadTexts:juniAutoConfMIB.setRevisions(('2004-07-26 19:54','2002-11-22 16:08','2002-11-22 15:24','2000-11-16 00:00'))
class JuniAutoConfEncaps(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,17,19)));namedValues=NamedValues(*(('ip',0),('ppp',1),('pppoe',17),('bridgedEthernet',19)))
_JuniAutoConfObjects_ObjectIdentity=ObjectIdentity
juniAutoConfObjects=_JuniAutoConfObjects_ObjectIdentity((1,3,6,1,4,1,4874,2,2,48,1))
_JuniAutoConf_ObjectIdentity=ObjectIdentity
juniAutoConf=_JuniAutoConf_ObjectIdentity((1,3,6,1,4,1,4874,2,2,48,1,1))
_JuniAutoConfTable_Object=MibTable
juniAutoConfTable=_JuniAutoConfTable_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1))
if mibBuilder.loadTexts:juniAutoConfTable.setStatus(_A)
_JuniAutoConfEntry_Object=MibTableRow
juniAutoConfEntry=_JuniAutoConfEntry_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1))
juniAutoConfEntry.setIndexNames((0,_B,_F),(0,_B,_G))
if mibBuilder.loadTexts:juniAutoConfEntry.setStatus(_A)
_JuniAutoConfIfIndex_Type=InterfaceIndex
_JuniAutoConfIfIndex_Object=MibTableColumn
juniAutoConfIfIndex=_JuniAutoConfIfIndex_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,1),_JuniAutoConfIfIndex_Type())
juniAutoConfIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:juniAutoConfIfIndex.setStatus(_A)
_JuniAutoConfEncaps_Type=JuniAutoConfEncaps
_JuniAutoConfEncaps_Object=MibTableColumn
juniAutoConfEncaps=_JuniAutoConfEncaps_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,2),_JuniAutoConfEncaps_Type())
juniAutoConfEncaps.setMaxAccess(_H)
if mibBuilder.loadTexts:juniAutoConfEncaps.setStatus(_A)
_JuniAutoConfEnable_Type=JuniEnable
_JuniAutoConfEnable_Object=MibTableColumn
juniAutoConfEnable=_JuniAutoConfEnable_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,3),_JuniAutoConfEnable_Type())
juniAutoConfEnable.setMaxAccess(_E)
if mibBuilder.loadTexts:juniAutoConfEnable.setStatus(_A)
_JuniAutoConfLockoutSupported_Type=TruthValue
_JuniAutoConfLockoutSupported_Object=MibTableColumn
juniAutoConfLockoutSupported=_JuniAutoConfLockoutSupported_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,4),_JuniAutoConfLockoutSupported_Type())
juniAutoConfLockoutSupported.setMaxAccess(_D)
if mibBuilder.loadTexts:juniAutoConfLockoutSupported.setStatus(_A)
class _JuniAutoConfLockoutMin_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniAutoConfLockoutMin_Type.__name__=_C
_JuniAutoConfLockoutMin_Object=MibTableColumn
juniAutoConfLockoutMin=_JuniAutoConfLockoutMin_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,5),_JuniAutoConfLockoutMin_Type())
juniAutoConfLockoutMin.setMaxAccess(_E)
if mibBuilder.loadTexts:juniAutoConfLockoutMin.setStatus(_A)
class _JuniAutoConfLockoutMax_Type(Integer32):defaultValue=300;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniAutoConfLockoutMax_Type.__name__=_C
_JuniAutoConfLockoutMax_Object=MibTableColumn
juniAutoConfLockoutMax=_JuniAutoConfLockoutMax_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,6),_JuniAutoConfLockoutMax_Type())
juniAutoConfLockoutMax.setMaxAccess(_E)
if mibBuilder.loadTexts:juniAutoConfLockoutMax.setStatus(_A)
class _JuniAutoConfLockoutTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniAutoConfLockoutTime_Type.__name__=_C
_JuniAutoConfLockoutTime_Object=MibTableColumn
juniAutoConfLockoutTime=_JuniAutoConfLockoutTime_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,7),_JuniAutoConfLockoutTime_Type())
juniAutoConfLockoutTime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniAutoConfLockoutTime.setStatus(_A)
class _JuniAutoConfLockoutElapsedTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniAutoConfLockoutElapsedTime_Type.__name__=_C
_JuniAutoConfLockoutElapsedTime_Object=MibTableColumn
juniAutoConfLockoutElapsedTime=_JuniAutoConfLockoutElapsedTime_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,8),_JuniAutoConfLockoutElapsedTime_Type())
juniAutoConfLockoutElapsedTime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniAutoConfLockoutElapsedTime.setStatus(_A)
class _JuniAutoConfNextLockoutTime_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,86400))
_JuniAutoConfNextLockoutTime_Type.__name__=_C
_JuniAutoConfNextLockoutTime_Object=MibTableColumn
juniAutoConfNextLockoutTime=_JuniAutoConfNextLockoutTime_Object((1,3,6,1,4,1,4874,2,2,48,1,1,1,1,9),_JuniAutoConfNextLockoutTime_Type())
juniAutoConfNextLockoutTime.setMaxAccess(_D)
if mibBuilder.loadTexts:juniAutoConfNextLockoutTime.setStatus(_A)
_JuniAutoConfMIBConformance_ObjectIdentity=ObjectIdentity
juniAutoConfMIBConformance=_JuniAutoConfMIBConformance_ObjectIdentity((1,3,6,1,4,1,4874,2,2,48,4))
_JuniAutoConfMIBCompliances_ObjectIdentity=ObjectIdentity
juniAutoConfMIBCompliances=_JuniAutoConfMIBCompliances_ObjectIdentity((1,3,6,1,4,1,4874,2,2,48,4,1))
_JuniAutoConfMIBGroups_ObjectIdentity=ObjectIdentity
juniAutoConfMIBGroups=_JuniAutoConfMIBGroups_ObjectIdentity((1,3,6,1,4,1,4874,2,2,48,4,2))
juniAutoConfGroup=ObjectGroup((1,3,6,1,4,1,4874,2,2,48,4,2,1))
juniAutoConfGroup.setObjects((_B,_I))
if mibBuilder.loadTexts:juniAutoConfGroup.setStatus(_J)
juniAutoConfGroup2=ObjectGroup((1,3,6,1,4,1,4874,2,2,48,4,2,2))
juniAutoConfGroup2.setObjects(*((_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O),(_B,_P)))
if mibBuilder.loadTexts:juniAutoConfGroup2.setStatus(_A)
juniAutoConfCompliance=ModuleCompliance((1,3,6,1,4,1,4874,2,2,48,4,1,1))
juniAutoConfCompliance.setObjects((_B,_Q))
if mibBuilder.loadTexts:juniAutoConfCompliance.setStatus(_J)
juniAutoConfCompliance2=ModuleCompliance((1,3,6,1,4,1,4874,2,2,48,4,1,2))
juniAutoConfCompliance2.setObjects((_B,_R))
if mibBuilder.loadTexts:juniAutoConfCompliance2.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'JuniAutoConfEncaps':JuniAutoConfEncaps,'juniAutoConfMIB':juniAutoConfMIB,'juniAutoConfObjects':juniAutoConfObjects,'juniAutoConf':juniAutoConf,'juniAutoConfTable':juniAutoConfTable,'juniAutoConfEntry':juniAutoConfEntry,_F:juniAutoConfIfIndex,_G:juniAutoConfEncaps,_I:juniAutoConfEnable,_K:juniAutoConfLockoutSupported,_L:juniAutoConfLockoutMin,_M:juniAutoConfLockoutMax,_N:juniAutoConfLockoutTime,_O:juniAutoConfLockoutElapsedTime,_P:juniAutoConfNextLockoutTime,'juniAutoConfMIBConformance':juniAutoConfMIBConformance,'juniAutoConfMIBCompliances':juniAutoConfMIBCompliances,'juniAutoConfCompliance':juniAutoConfCompliance,'juniAutoConfCompliance2':juniAutoConfCompliance2,'juniAutoConfMIBGroups':juniAutoConfMIBGroups,_Q:juniAutoConfGroup,_R:juniAutoConfGroup2})