_M='wwpLeosLagProtectionPort'
_L='wwpLeosLagPhyPortId'
_K='enhanced'
_J='DisplayString'
_I='manual'
_H='lacp'
_G='read-create'
_F='wwpLeosExtAggId'
_E='WWP-LEOS-EXT-LAG-MIB'
_D='read-write'
_C='read-only'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_J,'PhysAddress','RowStatus','TextualConvention')
wwpModulesLeos,=mibBuilder.importSymbols('WWP-SMI','wwpModulesLeos')
wwpLeosExtLagMIB=ModuleIdentity((1,3,6,1,4,1,6141,2,60,14))
if mibBuilder.loadTexts:wwpLeosExtLagMIB.setRevisions(('2003-01-15 17:00',))
_WwpLeosExtLagMIBObjects_ObjectIdentity=ObjectIdentity
wwpLeosExtLagMIBObjects=_WwpLeosExtLagMIBObjects_ObjectIdentity((1,3,6,1,4,1,6141,2,60,14,1))
_WwpLeosExtLag_ObjectIdentity=ObjectIdentity
wwpLeosExtLag=_WwpLeosExtLag_ObjectIdentity((1,3,6,1,4,1,6141,2,60,14,1,1))
_WwpLeosMaxLags_Type=Unsigned32
_WwpLeosMaxLags_Object=MibScalar
wwpLeosMaxLags=_WwpLeosMaxLags_Object((1,3,6,1,4,1,6141,2,60,14,1,1,1),_WwpLeosMaxLags_Type())
wwpLeosMaxLags.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosMaxLags.setStatus(_A)
_WwpLeosNumLags_Type=Unsigned32
_WwpLeosNumLags_Object=MibScalar
wwpLeosNumLags=_WwpLeosNumLags_Object((1,3,6,1,4,1,6141,2,60,14,1,1,2),_WwpLeosNumLags_Type())
wwpLeosNumLags.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosNumLags.setStatus(_A)
_WwpLeosExtLagTable_Object=MibTable
wwpLeosExtLagTable=_WwpLeosExtLagTable_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3))
if mibBuilder.loadTexts:wwpLeosExtLagTable.setStatus(_A)
_WwpLeosExtLagEntry_Object=MibTableRow
wwpLeosExtLagEntry=_WwpLeosExtLagEntry_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1))
wwpLeosExtLagEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:wwpLeosExtLagEntry.setStatus(_A)
class _WwpLeosExtAggId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpLeosExtAggId_Type.__name__=_B
_WwpLeosExtAggId_Object=MibTableColumn
wwpLeosExtAggId=_WwpLeosExtAggId_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,1),_WwpLeosExtAggId_Type())
wwpLeosExtAggId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosExtAggId.setStatus(_A)
class _WwpLeosExtAggName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_WwpLeosExtAggName_Type.__name__=_J
_WwpLeosExtAggName_Object=MibTableColumn
wwpLeosExtAggName=_WwpLeosExtAggName_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,2),_WwpLeosExtAggName_Type())
wwpLeosExtAggName.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosExtAggName.setStatus(_A)
class _WwpLeosExtAggIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_WwpLeosExtAggIndex_Type.__name__=_B
_WwpLeosExtAggIndex_Object=MibTableColumn
wwpLeosExtAggIndex=_WwpLeosExtAggIndex_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,3),_WwpLeosExtAggIndex_Type())
wwpLeosExtAggIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosExtAggIndex.setStatus(_A)
_WwpLeosExtAggStatus_Type=RowStatus
_WwpLeosExtAggStatus_Object=MibTableColumn
wwpLeosExtAggStatus=_WwpLeosExtAggStatus_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,4),_WwpLeosExtAggStatus_Type())
wwpLeosExtAggStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosExtAggStatus.setStatus(_A)
class _WwpLeosExtAggMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosExtAggMode_Type.__name__=_B
_WwpLeosExtAggMode_Object=MibTableColumn
wwpLeosExtAggMode=_WwpLeosExtAggMode_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,5),_WwpLeosExtAggMode_Type())
wwpLeosExtAggMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosExtAggMode.setStatus(_A)
class _WwpLeosExtLagProtectionRevertState_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('on',1),('off',2)))
_WwpLeosExtLagProtectionRevertState_Type.__name__=_B
_WwpLeosExtLagProtectionRevertState_Object=MibTableColumn
wwpLeosExtLagProtectionRevertState=_WwpLeosExtLagProtectionRevertState_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,6),_WwpLeosExtLagProtectionRevertState_Type())
wwpLeosExtLagProtectionRevertState.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosExtLagProtectionRevertState.setStatus(_A)
class _WwpLeosExtLagProtectionRevertTimer_Type(Integer32):defaultValue=5000;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,60000))
_WwpLeosExtLagProtectionRevertTimer_Type.__name__=_B
_WwpLeosExtLagProtectionRevertTimer_Object=MibTableColumn
wwpLeosExtLagProtectionRevertTimer=_WwpLeosExtLagProtectionRevertTimer_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,7),_WwpLeosExtLagProtectionRevertTimer_Type())
wwpLeosExtLagProtectionRevertTimer.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosExtLagProtectionRevertTimer.setStatus(_A)
if mibBuilder.loadTexts:wwpLeosExtLagProtectionRevertTimer.setUnits('msec')
class _WwpLeosExtAggHashMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('mac-based',1),('ip-based',2),(_K,3)))
_WwpLeosExtAggHashMode_Type.__name__=_B
_WwpLeosExtAggHashMode_Object=MibTableColumn
wwpLeosExtAggHashMode=_WwpLeosExtAggHashMode_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,8),_WwpLeosExtAggHashMode_Type())
wwpLeosExtAggHashMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosExtAggHashMode.setStatus(_A)
class _WwpLeosExtLagProtectionMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('proprietary',1),('standard',2)))
_WwpLeosExtLagProtectionMode_Type.__name__=_B
_WwpLeosExtLagProtectionMode_Object=MibTableColumn
wwpLeosExtLagProtectionMode=_WwpLeosExtLagProtectionMode_Object((1,3,6,1,4,1,6141,2,60,14,1,1,3,1,9),_WwpLeosExtLagProtectionMode_Type())
wwpLeosExtLagProtectionMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosExtLagProtectionMode.setStatus(_A)
_WwpLeosLagModeTable_Object=MibTable
wwpLeosLagModeTable=_WwpLeosLagModeTable_Object((1,3,6,1,4,1,6141,2,60,14,1,1,4))
if mibBuilder.loadTexts:wwpLeosLagModeTable.setStatus(_A)
_WwpLeosLagModeEntry_Object=MibTableRow
wwpLeosLagModeEntry=_WwpLeosLagModeEntry_Object((1,3,6,1,4,1,6141,2,60,14,1,1,4,1))
wwpLeosLagModeEntry.setIndexNames((0,_E,_L))
if mibBuilder.loadTexts:wwpLeosLagModeEntry.setStatus(_A)
class _WwpLeosLagPhyPortId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_WwpLeosLagPhyPortId_Type.__name__=_B
_WwpLeosLagPhyPortId_Object=MibTableColumn
wwpLeosLagPhyPortId=_WwpLeosLagPhyPortId_Object((1,3,6,1,4,1,6141,2,60,14,1,1,4,1,1),_WwpLeosLagPhyPortId_Type())
wwpLeosLagPhyPortId.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLagPhyPortId.setStatus(_A)
class _WwpLeosLagAdminMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosLagAdminMode_Type.__name__=_B
_WwpLeosLagAdminMode_Object=MibTableColumn
wwpLeosLagAdminMode=_WwpLeosLagAdminMode_Object((1,3,6,1,4,1,6141,2,60,14,1,1,4,1,2),_WwpLeosLagAdminMode_Type())
wwpLeosLagAdminMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosLagAdminMode.setStatus(_A)
class _WwpLeosLagOperMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_H,1),(_I,2)))
_WwpLeosLagOperMode_Type.__name__=_B
_WwpLeosLagOperMode_Object=MibTableColumn
wwpLeosLagOperMode=_WwpLeosLagOperMode_Object((1,3,6,1,4,1,6141,2,60,14,1,1,4,1,3),_WwpLeosLagOperMode_Type())
wwpLeosLagOperMode.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLagOperMode.setStatus(_A)
_WwpLeosLagProtectionTable_Object=MibTable
wwpLeosLagProtectionTable=_WwpLeosLagProtectionTable_Object((1,3,6,1,4,1,6141,2,60,14,1,1,5))
if mibBuilder.loadTexts:wwpLeosLagProtectionTable.setStatus(_A)
_WwpLeosLagProtectionEntry_Object=MibTableRow
wwpLeosLagProtectionEntry=_WwpLeosLagProtectionEntry_Object((1,3,6,1,4,1,6141,2,60,14,1,1,5,1))
wwpLeosLagProtectionEntry.setIndexNames((0,_E,_F),(0,_E,_M))
if mibBuilder.loadTexts:wwpLeosLagProtectionEntry.setStatus(_A)
class _WwpLeosLagProtectionPort_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_WwpLeosLagProtectionPort_Type.__name__=_B
_WwpLeosLagProtectionPort_Object=MibTableColumn
wwpLeosLagProtectionPort=_WwpLeosLagProtectionPort_Object((1,3,6,1,4,1,6141,2,60,14,1,1,5,1,1),_WwpLeosLagProtectionPort_Type())
wwpLeosLagProtectionPort.setMaxAccess(_C)
if mibBuilder.loadTexts:wwpLeosLagProtectionPort.setStatus(_A)
_WwpLeosLagProtectionRowStatus_Type=RowStatus
_WwpLeosLagProtectionRowStatus_Object=MibTableColumn
wwpLeosLagProtectionRowStatus=_WwpLeosLagProtectionRowStatus_Object((1,3,6,1,4,1,6141,2,60,14,1,1,5,1,2),_WwpLeosLagProtectionRowStatus_Type())
wwpLeosLagProtectionRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:wwpLeosLagProtectionRowStatus.setStatus(_A)
class _WwpLeosExtAggFloodHashMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('simplified',1),(_K,2)))
_WwpLeosExtAggFloodHashMode_Type.__name__=_B
_WwpLeosExtAggFloodHashMode_Object=MibScalar
wwpLeosExtAggFloodHashMode=_WwpLeosExtAggFloodHashMode_Object((1,3,6,1,4,1,6141,2,60,14,1,1,6),_WwpLeosExtAggFloodHashMode_Type())
wwpLeosExtAggFloodHashMode.setMaxAccess(_D)
if mibBuilder.loadTexts:wwpLeosExtAggFloodHashMode.setStatus(_A)
_WwpLeosExtLagMIBNotificationPrefix_ObjectIdentity=ObjectIdentity
wwpLeosExtLagMIBNotificationPrefix=_WwpLeosExtLagMIBNotificationPrefix_ObjectIdentity((1,3,6,1,4,1,6141,2,60,14,2))
_WwpLeosExtLagMIBNotifications_ObjectIdentity=ObjectIdentity
wwpLeosExtLagMIBNotifications=_WwpLeosExtLagMIBNotifications_ObjectIdentity((1,3,6,1,4,1,6141,2,60,14,2,0))
_WwpLeosExtLagMIBConformance_ObjectIdentity=ObjectIdentity
wwpLeosExtLagMIBConformance=_WwpLeosExtLagMIBConformance_ObjectIdentity((1,3,6,1,4,1,6141,2,60,14,3))
_WwpLeosExtLagMIBCompliances_ObjectIdentity=ObjectIdentity
wwpLeosExtLagMIBCompliances=_WwpLeosExtLagMIBCompliances_ObjectIdentity((1,3,6,1,4,1,6141,2,60,14,3,1))
_WwpLeosExtLagMIBGroups_ObjectIdentity=ObjectIdentity
wwpLeosExtLagMIBGroups=_WwpLeosExtLagMIBGroups_ObjectIdentity((1,3,6,1,4,1,6141,2,60,14,3,2))
mibBuilder.exportSymbols(_E,**{'wwpLeosExtLagMIB':wwpLeosExtLagMIB,'wwpLeosExtLagMIBObjects':wwpLeosExtLagMIBObjects,'wwpLeosExtLag':wwpLeosExtLag,'wwpLeosMaxLags':wwpLeosMaxLags,'wwpLeosNumLags':wwpLeosNumLags,'wwpLeosExtLagTable':wwpLeosExtLagTable,'wwpLeosExtLagEntry':wwpLeosExtLagEntry,_F:wwpLeosExtAggId,'wwpLeosExtAggName':wwpLeosExtAggName,'wwpLeosExtAggIndex':wwpLeosExtAggIndex,'wwpLeosExtAggStatus':wwpLeosExtAggStatus,'wwpLeosExtAggMode':wwpLeosExtAggMode,'wwpLeosExtLagProtectionRevertState':wwpLeosExtLagProtectionRevertState,'wwpLeosExtLagProtectionRevertTimer':wwpLeosExtLagProtectionRevertTimer,'wwpLeosExtAggHashMode':wwpLeosExtAggHashMode,'wwpLeosExtLagProtectionMode':wwpLeosExtLagProtectionMode,'wwpLeosLagModeTable':wwpLeosLagModeTable,'wwpLeosLagModeEntry':wwpLeosLagModeEntry,_L:wwpLeosLagPhyPortId,'wwpLeosLagAdminMode':wwpLeosLagAdminMode,'wwpLeosLagOperMode':wwpLeosLagOperMode,'wwpLeosLagProtectionTable':wwpLeosLagProtectionTable,'wwpLeosLagProtectionEntry':wwpLeosLagProtectionEntry,_M:wwpLeosLagProtectionPort,'wwpLeosLagProtectionRowStatus':wwpLeosLagProtectionRowStatus,'wwpLeosExtAggFloodHashMode':wwpLeosExtAggFloodHashMode,'wwpLeosExtLagMIBNotificationPrefix':wwpLeosExtLagMIBNotificationPrefix,'wwpLeosExtLagMIBNotifications':wwpLeosExtLagMIBNotifications,'wwpLeosExtLagMIBConformance':wwpLeosExtLagMIBConformance,'wwpLeosExtLagMIBCompliances':wwpLeosExtLagMIBCompliances,'wwpLeosExtLagMIBGroups':wwpLeosExtLagMIBGroups})