_H='atiQosProfileIndex'
_G='CENTRECOM-QOS-MIB'
_F='DisplayString'
_E='atiVlanIfIndex'
_D='CENTRECOM-VLAN-MIB'
_C='Integer32'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
extSwitchMIB,=mibBuilder.importSymbols('CENTRECOM-MIB','extSwitchMIB')
atiVlanIfIndex,=mibBuilder.importSymbols(_D,_E)
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC',_F,'PhysAddress','RowStatus','TextualConvention','TruthValue')
atiQos=ModuleIdentity((1,3,6,1,4,1,207,8,12,2,5))
_AtiQosCommon_ObjectIdentity=ObjectIdentity
atiQosCommon=_AtiQosCommon_ObjectIdentity((1,3,6,1,4,1,207,8,12,2,5,1))
class _AtiQosMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('ingress',1),('egress',2)))
_AtiQosMode_Type.__name__=_C
_AtiQosMode_Object=MibScalar
atiQosMode=_AtiQosMode_Object((1,3,6,1,4,1,207,8,12,2,5,1,4),_AtiQosMode_Type())
atiQosMode.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosMode.setStatus(_A)
_AtiQosUnconfigure_Type=TruthValue
_AtiQosUnconfigure_Object=MibScalar
atiQosUnconfigure=_AtiQosUnconfigure_Object((1,3,6,1,4,1,207,8,12,2,5,1,5),_AtiQosUnconfigure_Type())
atiQosUnconfigure.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosUnconfigure.setStatus(_A)
_AtiQosProfileTable_Object=MibTable
atiQosProfileTable=_AtiQosProfileTable_Object((1,3,6,1,4,1,207,8,12,2,5,1,6))
if mibBuilder.loadTexts:atiQosProfileTable.setStatus(_A)
_AtiQosProfileEntry_Object=MibTableRow
atiQosProfileEntry=_AtiQosProfileEntry_Object((1,3,6,1,4,1,207,8,12,2,5,1,6,1))
atiQosProfileEntry.setIndexNames((0,_G,_H))
if mibBuilder.loadTexts:atiQosProfileEntry.setStatus(_A)
class _AtiQosProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiQosProfileIndex_Type.__name__=_C
_AtiQosProfileIndex_Object=MibTableColumn
atiQosProfileIndex=_AtiQosProfileIndex_Object((1,3,6,1,4,1,207,8,12,2,5,1,6,1,1),_AtiQosProfileIndex_Type())
atiQosProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosProfileIndex.setStatus(_A)
class _AtiQosProfileName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,127))
_AtiQosProfileName_Type.__name__=_F
_AtiQosProfileName_Object=MibTableColumn
atiQosProfileName=_AtiQosProfileName_Object((1,3,6,1,4,1,207,8,12,2,5,1,6,1,2),_AtiQosProfileName_Type())
atiQosProfileName.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosProfileName.setStatus(_A)
_AtiQosProfileMinBw_Type=Integer32
_AtiQosProfileMinBw_Object=MibTableColumn
atiQosProfileMinBw=_AtiQosProfileMinBw_Object((1,3,6,1,4,1,207,8,12,2,5,1,6,1,3),_AtiQosProfileMinBw_Type())
atiQosProfileMinBw.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosProfileMinBw.setStatus(_A)
_AtiQosProfileMaxBw_Type=Integer32
_AtiQosProfileMaxBw_Object=MibTableColumn
atiQosProfileMaxBw=_AtiQosProfileMaxBw_Object((1,3,6,1,4,1,207,8,12,2,5,1,6,1,4),_AtiQosProfileMaxBw_Type())
atiQosProfileMaxBw.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosProfileMaxBw.setStatus(_A)
class _AtiQosProfilePriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('low',1),('normal',2),('medium',3),('high',4)))
_AtiQosProfilePriority_Type.__name__=_C
_AtiQosProfilePriority_Object=MibTableColumn
atiQosProfilePriority=_AtiQosProfilePriority_Object((1,3,6,1,4,1,207,8,12,2,5,1,6,1,5),_AtiQosProfilePriority_Type())
atiQosProfilePriority.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosProfilePriority.setStatus(_A)
_AtiQosProfileRowStatus_Type=RowStatus
_AtiQosProfileRowStatus_Object=MibTableColumn
atiQosProfileRowStatus=_AtiQosProfileRowStatus_Object((1,3,6,1,4,1,207,8,12,2,5,1,6,1,6),_AtiQosProfileRowStatus_Type())
atiQosProfileRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosProfileRowStatus.setStatus(_A)
_AtiQosByVlanMappingTable_Object=MibTable
atiQosByVlanMappingTable=_AtiQosByVlanMappingTable_Object((1,3,6,1,4,1,207,8,12,2,5,1,7))
if mibBuilder.loadTexts:atiQosByVlanMappingTable.setStatus(_A)
_AtiQosByVlanMappingEntry_Object=MibTableRow
atiQosByVlanMappingEntry=_AtiQosByVlanMappingEntry_Object((1,3,6,1,4,1,207,8,12,2,5,1,7,1))
atiQosByVlanMappingEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:atiQosByVlanMappingEntry.setStatus(_A)
class _AtiQosByVlanMappingQosProfileIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,65535))
_AtiQosByVlanMappingQosProfileIndex_Type.__name__=_C
_AtiQosByVlanMappingQosProfileIndex_Object=MibTableColumn
atiQosByVlanMappingQosProfileIndex=_AtiQosByVlanMappingQosProfileIndex_Object((1,3,6,1,4,1,207,8,12,2,5,1,7,1,1),_AtiQosByVlanMappingQosProfileIndex_Type())
atiQosByVlanMappingQosProfileIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:atiQosByVlanMappingQosProfileIndex.setStatus(_A)
mibBuilder.exportSymbols(_G,**{'atiQos':atiQos,'atiQosCommon':atiQosCommon,'atiQosMode':atiQosMode,'atiQosUnconfigure':atiQosUnconfigure,'atiQosProfileTable':atiQosProfileTable,'atiQosProfileEntry':atiQosProfileEntry,_H:atiQosProfileIndex,'atiQosProfileName':atiQosProfileName,'atiQosProfileMinBw':atiQosProfileMinBw,'atiQosProfileMaxBw':atiQosProfileMaxBw,'atiQosProfilePriority':atiQosProfilePriority,'atiQosProfileRowStatus':atiQosProfileRowStatus,'atiQosByVlanMappingTable':atiQosByVlanMappingTable,'atiQosByVlanMappingEntry':atiQosByVlanMappingEntry,'atiQosByVlanMappingQosProfileIndex':atiQosByVlanMappingQosProfileIndex})