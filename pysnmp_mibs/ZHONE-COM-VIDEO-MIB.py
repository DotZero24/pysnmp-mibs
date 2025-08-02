_N='videoMulticastSourceIndexNext'
_M='videoMulticastSourceNetMask'
_L='videoMulticastSourceIpAddress'
_K='videoMulticastSourceRowStatus'
_J='videoInterfaceType'
_I='videoInterfaceRowStatus'
_H='videoMulticastSourceIndex'
_G='read-create'
_F='ifIndex'
_E='IF-MIB'
_D='read-write'
_C='Integer32'
_B='ZHONE-COM-VIDEO-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ifIndex,ifPhysAddress=mibBuilder.importSymbols(_E,_F,'ifPhysAddress')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
zhoneModules,zhoneVideo=mibBuilder.importSymbols('Zhone','zhoneModules','zhoneVideo')
ZhoneRowStatus,=mibBuilder.importSymbols('Zhone-TC','ZhoneRowStatus')
comVideo=ModuleIdentity((1,3,6,1,4,1,5504,6,78))
if mibBuilder.loadTexts:comVideo.setRevisions(('2003-10-28 11:00',))
_VideoInterfaceTable_Object=MibTable
videoInterfaceTable=_VideoInterfaceTable_Object((1,3,6,1,4,1,5504,4,8,2))
if mibBuilder.loadTexts:videoInterfaceTable.setStatus(_A)
_VideoInterfaceEntry_Object=MibTableRow
videoInterfaceEntry=_VideoInterfaceEntry_Object((1,3,6,1,4,1,5504,4,8,2,1))
videoInterfaceEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:videoInterfaceEntry.setStatus(_A)
_VideoInterfaceRowStatus_Type=ZhoneRowStatus
_VideoInterfaceRowStatus_Object=MibTableColumn
videoInterfaceRowStatus=_VideoInterfaceRowStatus_Object((1,3,6,1,4,1,5504,4,8,2,1,1),_VideoInterfaceRowStatus_Type())
videoInterfaceRowStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:videoInterfaceRowStatus.setStatus(_A)
class _VideoInterfaceType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('management',1),('stream',2),('client',3)))
_VideoInterfaceType_Type.__name__=_C
_VideoInterfaceType_Object=MibTableColumn
videoInterfaceType=_VideoInterfaceType_Object((1,3,6,1,4,1,5504,4,8,2,1,2),_VideoInterfaceType_Type())
videoInterfaceType.setMaxAccess(_G)
if mibBuilder.loadTexts:videoInterfaceType.setStatus(_A)
_VideoMulticastSourceTable_Object=MibTable
videoMulticastSourceTable=_VideoMulticastSourceTable_Object((1,3,6,1,4,1,5504,4,8,3))
if mibBuilder.loadTexts:videoMulticastSourceTable.setStatus(_A)
_VideoMulticastSourceEntry_Object=MibTableRow
videoMulticastSourceEntry=_VideoMulticastSourceEntry_Object((1,3,6,1,4,1,5504,4,8,3,1))
videoMulticastSourceEntry.setIndexNames((0,_B,_H))
if mibBuilder.loadTexts:videoMulticastSourceEntry.setStatus(_A)
class _VideoMulticastSourceIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VideoMulticastSourceIndex_Type.__name__=_C
_VideoMulticastSourceIndex_Object=MibTableColumn
videoMulticastSourceIndex=_VideoMulticastSourceIndex_Object((1,3,6,1,4,1,5504,4,8,3,1,1),_VideoMulticastSourceIndex_Type())
videoMulticastSourceIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:videoMulticastSourceIndex.setStatus(_A)
_VideoMulticastSourceRowStatus_Type=ZhoneRowStatus
_VideoMulticastSourceRowStatus_Object=MibTableColumn
videoMulticastSourceRowStatus=_VideoMulticastSourceRowStatus_Object((1,3,6,1,4,1,5504,4,8,3,1,2),_VideoMulticastSourceRowStatus_Type())
videoMulticastSourceRowStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:videoMulticastSourceRowStatus.setStatus(_A)
_VideoMulticastSourceIpAddress_Type=IpAddress
_VideoMulticastSourceIpAddress_Object=MibTableColumn
videoMulticastSourceIpAddress=_VideoMulticastSourceIpAddress_Object((1,3,6,1,4,1,5504,4,8,3,1,3),_VideoMulticastSourceIpAddress_Type())
videoMulticastSourceIpAddress.setMaxAccess(_D)
if mibBuilder.loadTexts:videoMulticastSourceIpAddress.setStatus(_A)
_VideoMulticastSourceNetMask_Type=IpAddress
_VideoMulticastSourceNetMask_Object=MibTableColumn
videoMulticastSourceNetMask=_VideoMulticastSourceNetMask_Object((1,3,6,1,4,1,5504,4,8,3,1,4),_VideoMulticastSourceNetMask_Type())
videoMulticastSourceNetMask.setMaxAccess(_D)
if mibBuilder.loadTexts:videoMulticastSourceNetMask.setStatus(_A)
class _VideoMulticastSourceIndexNext_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,2147483647))
_VideoMulticastSourceIndexNext_Type.__name__=_C
_VideoMulticastSourceIndexNext_Object=MibScalar
videoMulticastSourceIndexNext=_VideoMulticastSourceIndexNext_Object((1,3,6,1,4,1,5504,4,8,4),_VideoMulticastSourceIndexNext_Type())
videoMulticastSourceIndexNext.setMaxAccess('read-only')
if mibBuilder.loadTexts:videoMulticastSourceIndexNext.setStatus(_A)
videoGroup=ObjectGroup((1,3,6,1,4,1,5504,4,8,1))
videoGroup.setObjects(*((_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N)))
if mibBuilder.loadTexts:videoGroup.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'videoGroup':videoGroup,'videoInterfaceTable':videoInterfaceTable,'videoInterfaceEntry':videoInterfaceEntry,_I:videoInterfaceRowStatus,_J:videoInterfaceType,'videoMulticastSourceTable':videoMulticastSourceTable,'videoMulticastSourceEntry':videoMulticastSourceEntry,_H:videoMulticastSourceIndex,_K:videoMulticastSourceRowStatus,_L:videoMulticastSourceIpAddress,_M:videoMulticastSourceNetMask,_N:videoMulticastSourceIndexNext,'comVideo':comVideo})