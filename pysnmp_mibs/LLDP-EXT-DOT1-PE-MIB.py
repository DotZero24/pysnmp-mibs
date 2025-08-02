_V='lldpXdot1PeGroup'
_U='lldpXdot1PeRemPECSPAddress'
_T='lldpXdot1PeRemPEAddress'
_S='lldpXdot1PeRemPECascadePortPriority'
_R='lldpXdot1PeLocPECSPAddress'
_Q='lldpXdot1PeLocPEAddress'
_P='lldpXdot1PeLocPECascadePortPriority'
_O='lldpXdot1PeConfigPortExtensionTxEnable'
_N='lldpXdot1PeConfigPortExtensionEntry'
_M='read-write'
_L='TruthValue'
_K='lldpV2RemTimeMark'
_J='lldpV2RemLocalIfIndex'
_I='lldpV2RemLocalDestMACAddress'
_H='lldpV2RemIndex'
_G='lldpV2LocPortIfIndex'
_F='ifGeneralInformationGroup'
_E='Unsigned32'
_D='read-only'
_C='LLDP-V2-MIB'
_B='LLDP-EXT-DOT1-PE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifGeneralInformationGroup,=mibBuilder.importSymbols('IF-MIB',_F)
lldpXdot1StandAloneExtensions,=mibBuilder.importSymbols('LLDP-EXT-DOT1-EVB-EXTENSIONS-MIB','lldpXdot1StandAloneExtensions')
lldpV2Extensions,lldpV2LocPortIfIndex,lldpV2PortConfigEntry,lldpV2RemIndex,lldpV2RemLocalDestMACAddress,lldpV2RemLocalIfIndex,lldpV2RemTimeMark=mibBuilder.importSymbols(_C,'lldpV2Extensions',_G,'lldpV2PortConfigEntry',_H,_I,_J,_K)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_E,'iso')
DisplayString,MacAddress,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','MacAddress','PhysAddress','TextualConvention',_L)
lldpXDot1PEExtensions=ModuleIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2))
if mibBuilder.loadTexts:lldpXDot1PEExtensions.setRevisions(('2012-01-23 00:00',))
_LldpXdot1PeMIB_ObjectIdentity=ObjectIdentity
lldpXdot1PeMIB=_LldpXdot1PeMIB_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2,1))
_LldpXdot1PeObjects_ObjectIdentity=ObjectIdentity
lldpXdot1PeObjects=_LldpXdot1PeObjects_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1))
_LldpXdot1PeConfig_ObjectIdentity=ObjectIdentity
lldpXdot1PeConfig=_LldpXdot1PeConfig_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,1))
_LldpXdot1PeConfigPortExtensionTable_Object=MibTable
lldpXdot1PeConfigPortExtensionTable=_LldpXdot1PeConfigPortExtensionTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,1,1))
if mibBuilder.loadTexts:lldpXdot1PeConfigPortExtensionTable.setStatus(_A)
_LldpXdot1PeConfigPortExtensionEntry_Object=MibTableRow
lldpXdot1PeConfigPortExtensionEntry=_LldpXdot1PeConfigPortExtensionEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,1,1,1))
if mibBuilder.loadTexts:lldpXdot1PeConfigPortExtensionEntry.setStatus(_A)
class _LldpXdot1PeConfigPortExtensionTxEnable_Type(TruthValue):defaultValue=1
_LldpXdot1PeConfigPortExtensionTxEnable_Type.__name__=_L
_LldpXdot1PeConfigPortExtensionTxEnable_Object=MibTableColumn
lldpXdot1PeConfigPortExtensionTxEnable=_LldpXdot1PeConfigPortExtensionTxEnable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,1,1,1,1),_LldpXdot1PeConfigPortExtensionTxEnable_Type())
lldpXdot1PeConfigPortExtensionTxEnable.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpXdot1PeConfigPortExtensionTxEnable.setStatus(_A)
_LldpXdot1PeLocalData_ObjectIdentity=ObjectIdentity
lldpXdot1PeLocalData=_LldpXdot1PeLocalData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,2))
_LldpXdot1PeLocPortExtensionTable_Object=MibTable
lldpXdot1PeLocPortExtensionTable=_LldpXdot1PeLocPortExtensionTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,2,1))
if mibBuilder.loadTexts:lldpXdot1PeLocPortExtensionTable.setStatus(_A)
_LldpXdot1PeLocPortExtensionEntry_Object=MibTableRow
lldpXdot1PeLocPortExtensionEntry=_LldpXdot1PeLocPortExtensionEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,2,1,1))
lldpXdot1PeLocPortExtensionEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:lldpXdot1PeLocPortExtensionEntry.setStatus(_A)
class _LldpXdot1PeLocPECascadePortPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LldpXdot1PeLocPECascadePortPriority_Type.__name__=_E
_LldpXdot1PeLocPECascadePortPriority_Object=MibTableColumn
lldpXdot1PeLocPECascadePortPriority=_LldpXdot1PeLocPECascadePortPriority_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,2,1,1,1),_LldpXdot1PeLocPECascadePortPriority_Type())
lldpXdot1PeLocPECascadePortPriority.setMaxAccess(_M)
if mibBuilder.loadTexts:lldpXdot1PeLocPECascadePortPriority.setStatus(_A)
_LldpXdot1PeLocPEAddress_Type=MacAddress
_LldpXdot1PeLocPEAddress_Object=MibTableColumn
lldpXdot1PeLocPEAddress=_LldpXdot1PeLocPEAddress_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,2,1,1,2),_LldpXdot1PeLocPEAddress_Type())
lldpXdot1PeLocPEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1PeLocPEAddress.setStatus(_A)
_LldpXdot1PeLocPECSPAddress_Type=MacAddress
_LldpXdot1PeLocPECSPAddress_Object=MibTableColumn
lldpXdot1PeLocPECSPAddress=_LldpXdot1PeLocPECSPAddress_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,2,1,1,3),_LldpXdot1PeLocPECSPAddress_Type())
lldpXdot1PeLocPECSPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1PeLocPECSPAddress.setStatus(_A)
_LldpXdot1PeRemoteData_ObjectIdentity=ObjectIdentity
lldpXdot1PeRemoteData=_LldpXdot1PeRemoteData_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,3))
_LldpXdot1PeRemPortExtensionTable_Object=MibTable
lldpXdot1PeRemPortExtensionTable=_LldpXdot1PeRemPortExtensionTable_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,3,1))
if mibBuilder.loadTexts:lldpXdot1PeRemPortExtensionTable.setStatus(_A)
_LldpXdot1PeRemPortExtensionEntry_Object=MibTableRow
lldpXdot1PeRemPortExtensionEntry=_LldpXdot1PeRemPortExtensionEntry_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,3,1,1))
lldpXdot1PeRemPortExtensionEntry.setIndexNames((0,_C,_K),(0,_C,_J),(0,_C,_I),(0,_C,_H))
if mibBuilder.loadTexts:lldpXdot1PeRemPortExtensionEntry.setStatus(_A)
class _LldpXdot1PeRemPECascadePortPriority_Type(Unsigned32):subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_LldpXdot1PeRemPECascadePortPriority_Type.__name__=_E
_LldpXdot1PeRemPECascadePortPriority_Object=MibTableColumn
lldpXdot1PeRemPECascadePortPriority=_LldpXdot1PeRemPECascadePortPriority_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,3,1,1,1),_LldpXdot1PeRemPECascadePortPriority_Type())
lldpXdot1PeRemPECascadePortPriority.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1PeRemPECascadePortPriority.setStatus(_A)
_LldpXdot1PeRemPEAddress_Type=MacAddress
_LldpXdot1PeRemPEAddress_Object=MibTableColumn
lldpXdot1PeRemPEAddress=_LldpXdot1PeRemPEAddress_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,3,1,1,2),_LldpXdot1PeRemPEAddress_Type())
lldpXdot1PeRemPEAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1PeRemPEAddress.setStatus(_A)
_LldpXdot1PeRemPECSPAddress_Type=MacAddress
_LldpXdot1PeRemPECSPAddress_Object=MibTableColumn
lldpXdot1PeRemPECSPAddress=_LldpXdot1PeRemPECSPAddress_Object((1,3,111,2,802,1,1,13,1,5,32962,7,2,1,1,3,1,1,3),_LldpXdot1PeRemPECSPAddress_Type())
lldpXdot1PeRemPECSPAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:lldpXdot1PeRemPECSPAddress.setStatus(_A)
_LldpXdot1PeConformance_ObjectIdentity=ObjectIdentity
lldpXdot1PeConformance=_LldpXdot1PeConformance_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2,2))
_LldpXdot1PeCompliances_ObjectIdentity=ObjectIdentity
lldpXdot1PeCompliances=_LldpXdot1PeCompliances_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2,2,1))
_LldpXdot1PeGroups_ObjectIdentity=ObjectIdentity
lldpXdot1PeGroups=_LldpXdot1PeGroups_ObjectIdentity((1,3,111,2,802,1,1,13,1,5,32962,7,2,2,2))
lldpV2PortConfigEntry.registerAugmentions((_B,_N))
lldpXdot1PeConfigPortExtensionEntry.setIndexNames(*lldpV2PortConfigEntry.getIndexNames())
lldpXdot1PeGroup=ObjectGroup((1,3,111,2,802,1,1,13,1,5,32962,7,2,2,2,1))
lldpXdot1PeGroup.setObjects(*((_B,_O),(_B,_P),(_B,_Q),(_B,_R),(_B,_S),(_B,_T),(_B,_U)))
if mibBuilder.loadTexts:lldpXdot1PeGroup.setStatus(_A)
lldpXdot1PeCompliance=ModuleCompliance((1,3,111,2,802,1,1,13,1,5,32962,7,2,2,1,1))
lldpXdot1PeCompliance.setObjects(*((_B,_V),(_B,_F)))
if mibBuilder.loadTexts:lldpXdot1PeCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'lldpXDot1PEExtensions':lldpXDot1PEExtensions,'lldpXdot1PeMIB':lldpXdot1PeMIB,'lldpXdot1PeObjects':lldpXdot1PeObjects,'lldpXdot1PeConfig':lldpXdot1PeConfig,'lldpXdot1PeConfigPortExtensionTable':lldpXdot1PeConfigPortExtensionTable,_N:lldpXdot1PeConfigPortExtensionEntry,_O:lldpXdot1PeConfigPortExtensionTxEnable,'lldpXdot1PeLocalData':lldpXdot1PeLocalData,'lldpXdot1PeLocPortExtensionTable':lldpXdot1PeLocPortExtensionTable,'lldpXdot1PeLocPortExtensionEntry':lldpXdot1PeLocPortExtensionEntry,_P:lldpXdot1PeLocPECascadePortPriority,_Q:lldpXdot1PeLocPEAddress,_R:lldpXdot1PeLocPECSPAddress,'lldpXdot1PeRemoteData':lldpXdot1PeRemoteData,'lldpXdot1PeRemPortExtensionTable':lldpXdot1PeRemPortExtensionTable,'lldpXdot1PeRemPortExtensionEntry':lldpXdot1PeRemPortExtensionEntry,_S:lldpXdot1PeRemPECascadePortPriority,_T:lldpXdot1PeRemPEAddress,_U:lldpXdot1PeRemPECSPAddress,'lldpXdot1PeConformance':lldpXdot1PeConformance,'lldpXdot1PeCompliances':lldpXdot1PeCompliances,'lldpXdot1PeCompliance':lldpXdot1PeCompliance,'lldpXdot1PeGroups':lldpXdot1PeGroups,_V:lldpXdot1PeGroup})