_K='zyMvrGroupName'
_J='read-create'
_I='not-accessible'
_H='dot1dBasePort'
_G='BRIDGE-MIB'
_F='Integer32'
_E='zyMvrVid'
_D='read-only'
_C='ZYXEL-MVR-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_G,_H)
InetAddress,InetAddressType=mibBuilder.importSymbols('INET-ADDRESS-MIB','InetAddress','InetAddressType')
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelMvr=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,55))
_ZyxelMvrSetup_ObjectIdentity=ObjectIdentity
zyxelMvrSetup=_ZyxelMvrSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,55,1))
_ZyMvrMaxNumberOfVlans_Type=Integer32
_ZyMvrMaxNumberOfVlans_Object=MibScalar
zyMvrMaxNumberOfVlans=_ZyMvrMaxNumberOfVlans_Object((1,3,6,1,4,1,890,1,15,3,55,1,1),_ZyMvrMaxNumberOfVlans_Type())
zyMvrMaxNumberOfVlans.setMaxAccess(_D)
if mibBuilder.loadTexts:zyMvrMaxNumberOfVlans.setStatus(_A)
_ZyxelMvrTable_Object=MibTable
zyxelMvrTable=_ZyxelMvrTable_Object((1,3,6,1,4,1,890,1,15,3,55,1,2))
if mibBuilder.loadTexts:zyxelMvrTable.setStatus(_A)
_ZyxelMvrEntry_Object=MibTableRow
zyxelMvrEntry=_ZyxelMvrEntry_Object((1,3,6,1,4,1,890,1,15,3,55,1,2,1))
zyxelMvrEntry.setIndexNames((0,_C,_E))
if mibBuilder.loadTexts:zyxelMvrEntry.setStatus(_A)
_ZyMvrVid_Type=Integer32
_ZyMvrVid_Object=MibTableColumn
zyMvrVid=_ZyMvrVid_Object((1,3,6,1,4,1,890,1,15,3,55,1,2,1,1),_ZyMvrVid_Type())
zyMvrVid.setMaxAccess(_I)
if mibBuilder.loadTexts:zyMvrVid.setStatus(_A)
_ZyMvrName_Type=DisplayString
_ZyMvrName_Object=MibTableColumn
zyMvrName=_ZyMvrName_Object((1,3,6,1,4,1,890,1,15,3,55,1,2,1,2),_ZyMvrName_Type())
zyMvrName.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMvrName.setStatus(_A)
class _ZyMvrMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('dynamic',0),('compatible',1)))
_ZyMvrMode_Type.__name__=_F
_ZyMvrMode_Object=MibTableColumn
zyMvrMode=_ZyMvrMode_Object((1,3,6,1,4,1,890,1,15,3,55,1,2,1,3),_ZyMvrMode_Type())
zyMvrMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMvrMode.setStatus(_A)
_ZyMvr8021pPriority_Type=Integer32
_ZyMvr8021pPriority_Object=MibTableColumn
zyMvr8021pPriority=_ZyMvr8021pPriority_Object((1,3,6,1,4,1,890,1,15,3,55,1,2,1,4),_ZyMvr8021pPriority_Type())
zyMvr8021pPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMvr8021pPriority.setStatus(_A)
_ZyMvrRowStatus_Type=RowStatus
_ZyMvrRowStatus_Object=MibTableColumn
zyMvrRowStatus=_ZyMvrRowStatus_Object((1,3,6,1,4,1,890,1,15,3,55,1,2,1,5),_ZyMvrRowStatus_Type())
zyMvrRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zyMvrRowStatus.setStatus(_A)
_ZyxelMvrPortTable_Object=MibTable
zyxelMvrPortTable=_ZyxelMvrPortTable_Object((1,3,6,1,4,1,890,1,15,3,55,1,3))
if mibBuilder.loadTexts:zyxelMvrPortTable.setStatus(_A)
_ZyxelMvrPortEntry_Object=MibTableRow
zyxelMvrPortEntry=_ZyxelMvrPortEntry_Object((1,3,6,1,4,1,890,1,15,3,55,1,3,1))
zyxelMvrPortEntry.setIndexNames((0,_C,_E),(0,_G,_H))
if mibBuilder.loadTexts:zyxelMvrPortEntry.setStatus(_A)
class _ZyMvrPortRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('none',1),('sourcePort',2),('receiverPort',3)))
_ZyMvrPortRole_Type.__name__=_F
_ZyMvrPortRole_Object=MibTableColumn
zyMvrPortRole=_ZyMvrPortRole_Object((1,3,6,1,4,1,890,1,15,3,55,1,3,1,1),_ZyMvrPortRole_Type())
zyMvrPortRole.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMvrPortRole.setStatus(_A)
_ZyMvrPortTagging_Type=EnabledStatus
_ZyMvrPortTagging_Object=MibTableColumn
zyMvrPortTagging=_ZyMvrPortTagging_Object((1,3,6,1,4,1,890,1,15,3,55,1,3,1,2),_ZyMvrPortTagging_Type())
zyMvrPortTagging.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMvrPortTagging.setStatus(_A)
_ZyMvrMaxNumberOfGroups_Type=Integer32
_ZyMvrMaxNumberOfGroups_Object=MibScalar
zyMvrMaxNumberOfGroups=_ZyMvrMaxNumberOfGroups_Object((1,3,6,1,4,1,890,1,15,3,55,1,4),_ZyMvrMaxNumberOfGroups_Type())
zyMvrMaxNumberOfGroups.setMaxAccess(_D)
if mibBuilder.loadTexts:zyMvrMaxNumberOfGroups.setStatus(_A)
_ZyxelMvrGroupTable_Object=MibTable
zyxelMvrGroupTable=_ZyxelMvrGroupTable_Object((1,3,6,1,4,1,890,1,15,3,55,1,5))
if mibBuilder.loadTexts:zyxelMvrGroupTable.setStatus(_A)
_ZyxelMvrGroupEntry_Object=MibTableRow
zyxelMvrGroupEntry=_ZyxelMvrGroupEntry_Object((1,3,6,1,4,1,890,1,15,3,55,1,5,1))
zyxelMvrGroupEntry.setIndexNames((0,_C,_E),(0,_C,_K))
if mibBuilder.loadTexts:zyxelMvrGroupEntry.setStatus(_A)
_ZyMvrGroupName_Type=DisplayString
_ZyMvrGroupName_Object=MibTableColumn
zyMvrGroupName=_ZyMvrGroupName_Object((1,3,6,1,4,1,890,1,15,3,55,1,5,1,1),_ZyMvrGroupName_Type())
zyMvrGroupName.setMaxAccess(_I)
if mibBuilder.loadTexts:zyMvrGroupName.setStatus(_A)
_ZyMvrGroupStartIpAddressType_Type=InetAddressType
_ZyMvrGroupStartIpAddressType_Object=MibTableColumn
zyMvrGroupStartIpAddressType=_ZyMvrGroupStartIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,55,1,5,1,2),_ZyMvrGroupStartIpAddressType_Type())
zyMvrGroupStartIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyMvrGroupStartIpAddressType.setStatus(_A)
_ZyMvrGroupStartIpAddress_Type=InetAddress
_ZyMvrGroupStartIpAddress_Object=MibTableColumn
zyMvrGroupStartIpAddress=_ZyMvrGroupStartIpAddress_Object((1,3,6,1,4,1,890,1,15,3,55,1,5,1,3),_ZyMvrGroupStartIpAddress_Type())
zyMvrGroupStartIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMvrGroupStartIpAddress.setStatus(_A)
_ZyMvrGroupEndIpAddressType_Type=InetAddressType
_ZyMvrGroupEndIpAddressType_Object=MibTableColumn
zyMvrGroupEndIpAddressType=_ZyMvrGroupEndIpAddressType_Object((1,3,6,1,4,1,890,1,15,3,55,1,5,1,4),_ZyMvrGroupEndIpAddressType_Type())
zyMvrGroupEndIpAddressType.setMaxAccess(_D)
if mibBuilder.loadTexts:zyMvrGroupEndIpAddressType.setStatus(_A)
_ZyMvrGroupEndIpAddress_Type=InetAddress
_ZyMvrGroupEndIpAddress_Object=MibTableColumn
zyMvrGroupEndIpAddress=_ZyMvrGroupEndIpAddress_Object((1,3,6,1,4,1,890,1,15,3,55,1,5,1,5),_ZyMvrGroupEndIpAddress_Type())
zyMvrGroupEndIpAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:zyMvrGroupEndIpAddress.setStatus(_A)
_ZyMvrGroupRowStatus_Type=RowStatus
_ZyMvrGroupRowStatus_Object=MibTableColumn
zyMvrGroupRowStatus=_ZyMvrGroupRowStatus_Object((1,3,6,1,4,1,890,1,15,3,55,1,5,1,6),_ZyMvrGroupRowStatus_Type())
zyMvrGroupRowStatus.setMaxAccess(_J)
if mibBuilder.loadTexts:zyMvrGroupRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelMvr':zyxelMvr,'zyxelMvrSetup':zyxelMvrSetup,'zyMvrMaxNumberOfVlans':zyMvrMaxNumberOfVlans,'zyxelMvrTable':zyxelMvrTable,'zyxelMvrEntry':zyxelMvrEntry,_E:zyMvrVid,'zyMvrName':zyMvrName,'zyMvrMode':zyMvrMode,'zyMvr8021pPriority':zyMvr8021pPriority,'zyMvrRowStatus':zyMvrRowStatus,'zyxelMvrPortTable':zyxelMvrPortTable,'zyxelMvrPortEntry':zyxelMvrPortEntry,'zyMvrPortRole':zyMvrPortRole,'zyMvrPortTagging':zyMvrPortTagging,'zyMvrMaxNumberOfGroups':zyMvrMaxNumberOfGroups,'zyxelMvrGroupTable':zyxelMvrGroupTable,'zyxelMvrGroupEntry':zyxelMvrGroupEntry,_K:zyMvrGroupName,'zyMvrGroupStartIpAddressType':zyMvrGroupStartIpAddressType,'zyMvrGroupStartIpAddress':zyMvrGroupStartIpAddress,'zyMvrGroupEndIpAddressType':zyMvrGroupEndIpAddressType,'zyMvrGroupEndIpAddress':zyMvrGroupEndIpAddress,'zyMvrGroupRowStatus':zyMvrGroupRowStatus})