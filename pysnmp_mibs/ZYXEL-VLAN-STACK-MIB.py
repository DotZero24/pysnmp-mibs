_Q='not-accessible'
_P='zySelectiveQinQCvid'
_O='zySelectiveQinQPort'
_N='priority7'
_M='priority6'
_L='priority5'
_K='priority4'
_J='priority3'
_I='priority2'
_H='priority1'
_G='priority0'
_F='dot1dBasePort'
_E='BRIDGE-MIB'
_D='ZYXEL-VLAN-STACK-MIB'
_C='Integer32'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_E,_F)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelVlanStack=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,89))
_ZyxelVlanStackSetup_ObjectIdentity=ObjectIdentity
zyxelVlanStackSetup=_ZyxelVlanStackSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,89,1))
_ZyVlanStackState_Type=EnabledStatus
_ZyVlanStackState_Object=MibScalar
zyVlanStackState=_ZyVlanStackState_Object((1,3,6,1,4,1,890,1,15,3,89,1,1),_ZyVlanStackState_Type())
zyVlanStackState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanStackState.setStatus(_A)
_ZyxelVlanStackPortTable_Object=MibTable
zyxelVlanStackPortTable=_ZyxelVlanStackPortTable_Object((1,3,6,1,4,1,890,1,15,3,89,1,2))
if mibBuilder.loadTexts:zyxelVlanStackPortTable.setStatus(_A)
_ZyxelVlanStackPortEntry_Object=MibTableRow
zyxelVlanStackPortEntry=_ZyxelVlanStackPortEntry_Object((1,3,6,1,4,1,890,1,15,3,89,1,2,1))
zyxelVlanStackPortEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelVlanStackPortEntry.setStatus(_A)
class _ZyVlanStackPortMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('normal',1),('access',2),('tunnel',3)))
_ZyVlanStackPortMode_Type.__name__=_C
_ZyVlanStackPortMode_Object=MibTableColumn
zyVlanStackPortMode=_ZyVlanStackPortMode_Object((1,3,6,1,4,1,890,1,15,3,89,1,2,1,1),_ZyVlanStackPortMode_Type())
zyVlanStackPortMode.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanStackPortMode.setStatus(_A)
_ZyVlanStackPortVid_Type=Integer32
_ZyVlanStackPortVid_Object=MibTableColumn
zyVlanStackPortVid=_ZyVlanStackPortVid_Object((1,3,6,1,4,1,890,1,15,3,89,1,2,1,2),_ZyVlanStackPortVid_Type())
zyVlanStackPortVid.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanStackPortVid.setStatus(_A)
class _ZyVlanStackPortPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7)))
_ZyVlanStackPortPriority_Type.__name__=_C
_ZyVlanStackPortPriority_Object=MibTableColumn
zyVlanStackPortPriority=_ZyVlanStackPortPriority_Object((1,3,6,1,4,1,890,1,15,3,89,1,2,1,3),_ZyVlanStackPortPriority_Type())
zyVlanStackPortPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanStackPortPriority.setStatus(_A)
_ZyVlanStackTunnelPortTpid_Type=Integer32
_ZyVlanStackTunnelPortTpid_Object=MibTableColumn
zyVlanStackTunnelPortTpid=_ZyVlanStackTunnelPortTpid_Object((1,3,6,1,4,1,890,1,15,3,89,1,2,1,4),_ZyVlanStackTunnelPortTpid_Type())
zyVlanStackTunnelPortTpid.setMaxAccess(_B)
if mibBuilder.loadTexts:zyVlanStackTunnelPortTpid.setStatus(_A)
_ZySelectiveQinQMaxNumberOfRules_Type=Integer32
_ZySelectiveQinQMaxNumberOfRules_Object=MibScalar
zySelectiveQinQMaxNumberOfRules=_ZySelectiveQinQMaxNumberOfRules_Object((1,3,6,1,4,1,890,1,15,3,89,1,3),_ZySelectiveQinQMaxNumberOfRules_Type())
zySelectiveQinQMaxNumberOfRules.setMaxAccess('read-only')
if mibBuilder.loadTexts:zySelectiveQinQMaxNumberOfRules.setStatus(_A)
_ZyxelSelectiveQinQTable_Object=MibTable
zyxelSelectiveQinQTable=_ZyxelSelectiveQinQTable_Object((1,3,6,1,4,1,890,1,15,3,89,1,4))
if mibBuilder.loadTexts:zyxelSelectiveQinQTable.setStatus(_A)
_ZyxelSelectiveQinQEntry_Object=MibTableRow
zyxelSelectiveQinQEntry=_ZyxelSelectiveQinQEntry_Object((1,3,6,1,4,1,890,1,15,3,89,1,4,1))
zyxelSelectiveQinQEntry.setIndexNames((0,_D,_O),(0,_D,_P))
if mibBuilder.loadTexts:zyxelSelectiveQinQEntry.setStatus(_A)
_ZySelectiveQinQName_Type=DisplayString
_ZySelectiveQinQName_Object=MibTableColumn
zySelectiveQinQName=_ZySelectiveQinQName_Object((1,3,6,1,4,1,890,1,15,3,89,1,4,1,1),_ZySelectiveQinQName_Type())
zySelectiveQinQName.setMaxAccess(_B)
if mibBuilder.loadTexts:zySelectiveQinQName.setStatus(_A)
_ZySelectiveQinQPort_Type=Integer32
_ZySelectiveQinQPort_Object=MibTableColumn
zySelectiveQinQPort=_ZySelectiveQinQPort_Object((1,3,6,1,4,1,890,1,15,3,89,1,4,1,2),_ZySelectiveQinQPort_Type())
zySelectiveQinQPort.setMaxAccess(_Q)
if mibBuilder.loadTexts:zySelectiveQinQPort.setStatus(_A)
_ZySelectiveQinQCvid_Type=Integer32
_ZySelectiveQinQCvid_Object=MibTableColumn
zySelectiveQinQCvid=_ZySelectiveQinQCvid_Object((1,3,6,1,4,1,890,1,15,3,89,1,4,1,3),_ZySelectiveQinQCvid_Type())
zySelectiveQinQCvid.setMaxAccess(_Q)
if mibBuilder.loadTexts:zySelectiveQinQCvid.setStatus(_A)
_ZySelectiveQinQSpvid_Type=Integer32
_ZySelectiveQinQSpvid_Object=MibTableColumn
zySelectiveQinQSpvid=_ZySelectiveQinQSpvid_Object((1,3,6,1,4,1,890,1,15,3,89,1,4,1,4),_ZySelectiveQinQSpvid_Type())
zySelectiveQinQSpvid.setMaxAccess(_B)
if mibBuilder.loadTexts:zySelectiveQinQSpvid.setStatus(_A)
class _ZySelectiveQinQPriority_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3,4,5,6,7)));namedValues=NamedValues(*((_G,0),(_H,1),(_I,2),(_J,3),(_K,4),(_L,5),(_M,6),(_N,7)))
_ZySelectiveQinQPriority_Type.__name__=_C
_ZySelectiveQinQPriority_Object=MibTableColumn
zySelectiveQinQPriority=_ZySelectiveQinQPriority_Object((1,3,6,1,4,1,890,1,15,3,89,1,4,1,5),_ZySelectiveQinQPriority_Type())
zySelectiveQinQPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zySelectiveQinQPriority.setStatus(_A)
_ZySelectiveQinQRowStatus_Type=RowStatus
_ZySelectiveQinQRowStatus_Object=MibTableColumn
zySelectiveQinQRowStatus=_ZySelectiveQinQRowStatus_Object((1,3,6,1,4,1,890,1,15,3,89,1,4,1,6),_ZySelectiveQinQRowStatus_Type())
zySelectiveQinQRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zySelectiveQinQRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'zyxelVlanStack':zyxelVlanStack,'zyxelVlanStackSetup':zyxelVlanStackSetup,'zyVlanStackState':zyVlanStackState,'zyxelVlanStackPortTable':zyxelVlanStackPortTable,'zyxelVlanStackPortEntry':zyxelVlanStackPortEntry,'zyVlanStackPortMode':zyVlanStackPortMode,'zyVlanStackPortVid':zyVlanStackPortVid,'zyVlanStackPortPriority':zyVlanStackPortPriority,'zyVlanStackTunnelPortTpid':zyVlanStackTunnelPortTpid,'zySelectiveQinQMaxNumberOfRules':zySelectiveQinQMaxNumberOfRules,'zyxelSelectiveQinQTable':zyxelSelectiveQinQTable,'zyxelSelectiveQinQEntry':zyxelSelectiveQinQEntry,'zySelectiveQinQName':zySelectiveQinQName,_O:zySelectiveQinQPort,_P:zySelectiveQinQCvid,'zySelectiveQinQSpvid':zySelectiveQinQSpvid,'zySelectiveQinQPriority':zySelectiveQinQPriority,'zySelectiveQinQRowStatus':zySelectiveQinQRowStatus})