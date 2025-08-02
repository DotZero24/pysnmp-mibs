_J='synologyiSCSITargetGroup'
_I='iSCSITargetConnectionStatus'
_H='iSCSITargetIQN'
_G='iSCSITargetName'
_F='iSCSITargetInfoIndex'
_E='Integer32'
_D='read-only'
_C='OctetString'
_B='SYNOLOGY-ISCSITarget-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_C,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
synologyiSCSITarget=ModuleIdentity((1,3,6,1,4,1,6574,110))
_Synology_ObjectIdentity=ObjectIdentity
synology=_Synology_ObjectIdentity((1,3,6,1,4,1,6574))
_ISCSITargetTable_Object=MibTable
iSCSITargetTable=_ISCSITargetTable_Object((1,3,6,1,4,1,6574,110,1))
if mibBuilder.loadTexts:iSCSITargetTable.setStatus(_A)
_ISCSITargetEntry_Object=MibTableRow
iSCSITargetEntry=_ISCSITargetEntry_Object((1,3,6,1,4,1,6574,110,1,1))
iSCSITargetEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:iSCSITargetEntry.setStatus(_A)
class _ISCSITargetInfoIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,2147483647))
_ISCSITargetInfoIndex_Type.__name__=_E
_ISCSITargetInfoIndex_Object=MibTableColumn
iSCSITargetInfoIndex=_ISCSITargetInfoIndex_Object((1,3,6,1,4,1,6574,110,1,1,1),_ISCSITargetInfoIndex_Type())
iSCSITargetInfoIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:iSCSITargetInfoIndex.setStatus(_A)
class _ISCSITargetName_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ISCSITargetName_Type.__name__=_C
_ISCSITargetName_Object=MibTableColumn
iSCSITargetName=_ISCSITargetName_Object((1,3,6,1,4,1,6574,110,1,1,2),_ISCSITargetName_Type())
iSCSITargetName.setMaxAccess(_D)
if mibBuilder.loadTexts:iSCSITargetName.setStatus(_A)
class _ISCSITargetIQN_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_ISCSITargetIQN_Type.__name__=_C
_ISCSITargetIQN_Object=MibTableColumn
iSCSITargetIQN=_ISCSITargetIQN_Object((1,3,6,1,4,1,6574,110,1,1,3),_ISCSITargetIQN_Type())
iSCSITargetIQN.setMaxAccess(_D)
if mibBuilder.loadTexts:iSCSITargetIQN.setStatus(_A)
class _ISCSITargetConnectionStatus_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,4096))
_ISCSITargetConnectionStatus_Type.__name__=_C
_ISCSITargetConnectionStatus_Object=MibTableColumn
iSCSITargetConnectionStatus=_ISCSITargetConnectionStatus_Object((1,3,6,1,4,1,6574,110,1,1,4),_ISCSITargetConnectionStatus_Type())
iSCSITargetConnectionStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:iSCSITargetConnectionStatus.setStatus(_A)
_SynologyiSCSITargetConformance_ObjectIdentity=ObjectIdentity
synologyiSCSITargetConformance=_SynologyiSCSITargetConformance_ObjectIdentity((1,3,6,1,4,1,6574,110,2))
_SynologyiSCSITargetCompliances_ObjectIdentity=ObjectIdentity
synologyiSCSITargetCompliances=_SynologyiSCSITargetCompliances_ObjectIdentity((1,3,6,1,4,1,6574,110,2,1))
_SynologyiSCSITargetGroups_ObjectIdentity=ObjectIdentity
synologyiSCSITargetGroups=_SynologyiSCSITargetGroups_ObjectIdentity((1,3,6,1,4,1,6574,110,2,2))
synologyiSCSITargetGroup=ObjectGroup((1,3,6,1,4,1,6574,110,2,2,1))
synologyiSCSITargetGroup.setObjects(*((_B,_G),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:synologyiSCSITargetGroup.setStatus(_A)
synologyiSCSITargetCompliance=ModuleCompliance((1,3,6,1,4,1,6574,110,2,1,1))
synologyiSCSITargetCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:synologyiSCSITargetCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'synology':synology,'synologyiSCSITarget':synologyiSCSITarget,'iSCSITargetTable':iSCSITargetTable,'iSCSITargetEntry':iSCSITargetEntry,_F:iSCSITargetInfoIndex,_G:iSCSITargetName,_H:iSCSITargetIQN,_I:iSCSITargetConnectionStatus,'synologyiSCSITargetConformance':synologyiSCSITargetConformance,'synologyiSCSITargetCompliances':synologyiSCSITargetCompliances,'synologyiSCSITargetCompliance':synologyiSCSITargetCompliance,'synologyiSCSITargetGroups':synologyiSCSITargetGroups,_J:synologyiSCSITargetGroup})