_S='clreCpeDot1dTpGroup'
_R='clreCpePortGroup'
_Q='clreCpePortOperProtected'
_P='clreCpePortAdminProtected'
_O='clreCpePortAdminDuplex'
_N='clreCpePortAdminSpeed'
_M='clreCpePortAdminStatus'
_L='clreCpeDot1dBasePortIfIndex'
_K='autoDetect'
_J='read-only'
_I='TruthValue'
_H='ifIndex'
_G='IF-MIB'
_F='dot1dTpFdbAddress'
_E='BRIDGE-MIB'
_D='read-write'
_C='Integer32'
_B='CISCO-LRE-CPE-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dTpFdbAddress,=mibBuilder.importSymbols(_E,_F)
ciscoMgmt,=mibBuilder.importSymbols('CISCO-SMI','ciscoMgmt')
InterfaceIndex,ifIndex=mibBuilder.importSymbols(_G,'InterfaceIndex',_H)
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_I)
ciscoLreCpeMIB=ModuleIdentity((1,3,6,1,4,1,9,9,340))
if mibBuilder.loadTexts:ciscoLreCpeMIB.setRevisions(('2003-03-12 00:00',))
_ClreCpeMIBNotifications_ObjectIdentity=ObjectIdentity
clreCpeMIBNotifications=_ClreCpeMIBNotifications_ObjectIdentity((1,3,6,1,4,1,9,9,340,0))
_ClreCpeMIBNotificationsPrefix_ObjectIdentity=ObjectIdentity
clreCpeMIBNotificationsPrefix=_ClreCpeMIBNotificationsPrefix_ObjectIdentity((1,3,6,1,4,1,9,9,340,0,0))
_CiscoLreCpeMIBObjects_ObjectIdentity=ObjectIdentity
ciscoLreCpeMIBObjects=_CiscoLreCpeMIBObjects_ObjectIdentity((1,3,6,1,4,1,9,9,340,1))
_ClreCpeDot1dTp_ObjectIdentity=ObjectIdentity
clreCpeDot1dTp=_ClreCpeDot1dTp_ObjectIdentity((1,3,6,1,4,1,9,9,340,1,1))
_ClreCpeDot1dTpFdbTable_Object=MibTable
clreCpeDot1dTpFdbTable=_ClreCpeDot1dTpFdbTable_Object((1,3,6,1,4,1,9,9,340,1,1,1))
if mibBuilder.loadTexts:clreCpeDot1dTpFdbTable.setStatus(_A)
_ClreCpeDot1dTpFdbEntry_Object=MibTableRow
clreCpeDot1dTpFdbEntry=_ClreCpeDot1dTpFdbEntry_Object((1,3,6,1,4,1,9,9,340,1,1,1,1))
clreCpeDot1dTpFdbEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:clreCpeDot1dTpFdbEntry.setStatus(_A)
_ClreCpeDot1dBasePortIfIndex_Type=InterfaceIndex
_ClreCpeDot1dBasePortIfIndex_Object=MibTableColumn
clreCpeDot1dBasePortIfIndex=_ClreCpeDot1dBasePortIfIndex_Object((1,3,6,1,4,1,9,9,340,1,1,1,1,1),_ClreCpeDot1dBasePortIfIndex_Type())
clreCpeDot1dBasePortIfIndex.setMaxAccess(_J)
if mibBuilder.loadTexts:clreCpeDot1dBasePortIfIndex.setStatus(_A)
_ClreCpePort_ObjectIdentity=ObjectIdentity
clreCpePort=_ClreCpePort_ObjectIdentity((1,3,6,1,4,1,9,9,340,1,2))
_ClreCpePortTable_Object=MibTable
clreCpePortTable=_ClreCpePortTable_Object((1,3,6,1,4,1,9,9,340,1,2,1))
if mibBuilder.loadTexts:clreCpePortTable.setStatus(_A)
_ClreCpePortEntry_Object=MibTableRow
clreCpePortEntry=_ClreCpePortEntry_Object((1,3,6,1,4,1,9,9,340,1,2,1,1))
clreCpePortEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:clreCpePortEntry.setStatus(_A)
class _ClreCpePortAdminStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('up',1),('down',2),('testing',3)))
_ClreCpePortAdminStatus_Type.__name__=_C
_ClreCpePortAdminStatus_Object=MibTableColumn
clreCpePortAdminStatus=_ClreCpePortAdminStatus_Object((1,3,6,1,4,1,9,9,340,1,2,1,1,1),_ClreCpePortAdminStatus_Type())
clreCpePortAdminStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:clreCpePortAdminStatus.setStatus(_A)
class _ClreCpePortAdminSpeed_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,10000000,100000000)));namedValues=NamedValues(*((_K,1),('s10000000',10000000),('s100000000',100000000)))
_ClreCpePortAdminSpeed_Type.__name__=_C
_ClreCpePortAdminSpeed_Object=MibTableColumn
clreCpePortAdminSpeed=_ClreCpePortAdminSpeed_Object((1,3,6,1,4,1,9,9,340,1,2,1,1,2),_ClreCpePortAdminSpeed_Type())
clreCpePortAdminSpeed.setMaxAccess(_D)
if mibBuilder.loadTexts:clreCpePortAdminSpeed.setStatus(_A)
class _ClreCpePortAdminDuplex_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*((_K,1),('fullDuplex',2),('halfDuplex',3)))
_ClreCpePortAdminDuplex_Type.__name__=_C
_ClreCpePortAdminDuplex_Object=MibTableColumn
clreCpePortAdminDuplex=_ClreCpePortAdminDuplex_Object((1,3,6,1,4,1,9,9,340,1,2,1,1,3),_ClreCpePortAdminDuplex_Type())
clreCpePortAdminDuplex.setMaxAccess(_D)
if mibBuilder.loadTexts:clreCpePortAdminDuplex.setStatus(_A)
class _ClreCpePortAdminProtected_Type(TruthValue):defaultValue=2
_ClreCpePortAdminProtected_Type.__name__=_I
_ClreCpePortAdminProtected_Object=MibTableColumn
clreCpePortAdminProtected=_ClreCpePortAdminProtected_Object((1,3,6,1,4,1,9,9,340,1,2,1,1,4),_ClreCpePortAdminProtected_Type())
clreCpePortAdminProtected.setMaxAccess(_D)
if mibBuilder.loadTexts:clreCpePortAdminProtected.setStatus(_A)
_ClreCpePortOperProtected_Type=TruthValue
_ClreCpePortOperProtected_Object=MibTableColumn
clreCpePortOperProtected=_ClreCpePortOperProtected_Object((1,3,6,1,4,1,9,9,340,1,2,1,1,5),_ClreCpePortOperProtected_Type())
clreCpePortOperProtected.setMaxAccess(_J)
if mibBuilder.loadTexts:clreCpePortOperProtected.setStatus(_A)
_ClreCpeMIBConformance_ObjectIdentity=ObjectIdentity
clreCpeMIBConformance=_ClreCpeMIBConformance_ObjectIdentity((1,3,6,1,4,1,9,9,340,2))
_ClreCpeMIBCompliances_ObjectIdentity=ObjectIdentity
clreCpeMIBCompliances=_ClreCpeMIBCompliances_ObjectIdentity((1,3,6,1,4,1,9,9,340,2,1))
_ClreCpeMIBGroups_ObjectIdentity=ObjectIdentity
clreCpeMIBGroups=_ClreCpeMIBGroups_ObjectIdentity((1,3,6,1,4,1,9,9,340,2,2))
clreCpeDot1dTpGroup=ObjectGroup((1,3,6,1,4,1,9,9,340,2,2,1))
clreCpeDot1dTpGroup.setObjects((_B,_L))
if mibBuilder.loadTexts:clreCpeDot1dTpGroup.setStatus(_A)
clreCpePortGroup=ObjectGroup((1,3,6,1,4,1,9,9,340,2,2,2))
clreCpePortGroup.setObjects(*((_B,_M),(_B,_N),(_B,_O),(_B,_P),(_B,_Q)))
if mibBuilder.loadTexts:clreCpePortGroup.setStatus(_A)
clreCpeMIBCompliance=ModuleCompliance((1,3,6,1,4,1,9,9,340,2,1,1))
clreCpeMIBCompliance.setObjects(*((_B,_R),(_B,_S)))
if mibBuilder.loadTexts:clreCpeMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'ciscoLreCpeMIB':ciscoLreCpeMIB,'clreCpeMIBNotifications':clreCpeMIBNotifications,'clreCpeMIBNotificationsPrefix':clreCpeMIBNotificationsPrefix,'ciscoLreCpeMIBObjects':ciscoLreCpeMIBObjects,'clreCpeDot1dTp':clreCpeDot1dTp,'clreCpeDot1dTpFdbTable':clreCpeDot1dTpFdbTable,'clreCpeDot1dTpFdbEntry':clreCpeDot1dTpFdbEntry,_L:clreCpeDot1dBasePortIfIndex,'clreCpePort':clreCpePort,'clreCpePortTable':clreCpePortTable,'clreCpePortEntry':clreCpePortEntry,_M:clreCpePortAdminStatus,_N:clreCpePortAdminSpeed,_O:clreCpePortAdminDuplex,_P:clreCpePortAdminProtected,_Q:clreCpePortOperProtected,'clreCpeMIBConformance':clreCpeMIBConformance,'clreCpeMIBCompliances':clreCpeMIBCompliances,'clreCpeMIBCompliance':clreCpeMIBCompliance,'clreCpeMIBGroups':clreCpeMIBGroups,_S:clreCpeDot1dTpGroup,_R:clreCpePortGroup})