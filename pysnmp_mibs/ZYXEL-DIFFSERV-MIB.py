_F='zyDiffservMapDscp'
_E='ZYXEL-DIFFSERV-MIB'
_D='dot1dBasePort'
_C='BRIDGE-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_C,_D)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelDiffserv=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,22))
_ZyxelDiffservSetup_ObjectIdentity=ObjectIdentity
zyxelDiffservSetup=_ZyxelDiffservSetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,22,1))
_ZyDiffservState_Type=EnabledStatus
_ZyDiffservState_Object=MibScalar
zyDiffservState=_ZyDiffservState_Object((1,3,6,1,4,1,890,1,15,3,22,1,1),_ZyDiffservState_Type())
zyDiffservState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDiffservState.setStatus(_A)
_ZyxelDiffservMapTable_Object=MibTable
zyxelDiffservMapTable=_ZyxelDiffservMapTable_Object((1,3,6,1,4,1,890,1,15,3,22,1,2))
if mibBuilder.loadTexts:zyxelDiffservMapTable.setStatus(_A)
_ZyxelDiffservMapEntry_Object=MibTableRow
zyxelDiffservMapEntry=_ZyxelDiffservMapEntry_Object((1,3,6,1,4,1,890,1,15,3,22,1,2,1))
zyxelDiffservMapEntry.setIndexNames((0,_E,_F))
if mibBuilder.loadTexts:zyxelDiffservMapEntry.setStatus(_A)
_ZyDiffservMapDscp_Type=Integer32
_ZyDiffservMapDscp_Object=MibTableColumn
zyDiffservMapDscp=_ZyDiffservMapDscp_Object((1,3,6,1,4,1,890,1,15,3,22,1,2,1,1),_ZyDiffservMapDscp_Type())
zyDiffservMapDscp.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:zyDiffservMapDscp.setStatus(_A)
_ZyDiffservMapPriority_Type=Integer32
_ZyDiffservMapPriority_Object=MibTableColumn
zyDiffservMapPriority=_ZyDiffservMapPriority_Object((1,3,6,1,4,1,890,1,15,3,22,1,2,1,2),_ZyDiffservMapPriority_Type())
zyDiffservMapPriority.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDiffservMapPriority.setStatus(_A)
_ZyxelDiffservPortTable_Object=MibTable
zyxelDiffservPortTable=_ZyxelDiffservPortTable_Object((1,3,6,1,4,1,890,1,15,3,22,1,3))
if mibBuilder.loadTexts:zyxelDiffservPortTable.setStatus(_A)
_ZyxelDiffservPortEntry_Object=MibTableRow
zyxelDiffservPortEntry=_ZyxelDiffservPortEntry_Object((1,3,6,1,4,1,890,1,15,3,22,1,3,1))
zyxelDiffservPortEntry.setIndexNames((0,_C,_D))
if mibBuilder.loadTexts:zyxelDiffservPortEntry.setStatus(_A)
_ZyDiffservPortState_Type=EnabledStatus
_ZyDiffservPortState_Object=MibTableColumn
zyDiffservPortState=_ZyDiffservPortState_Object((1,3,6,1,4,1,890,1,15,3,22,1,3,1,1),_ZyDiffservPortState_Type())
zyDiffservPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyDiffservPortState.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'zyxelDiffserv':zyxelDiffserv,'zyxelDiffservSetup':zyxelDiffservSetup,'zyDiffservState':zyDiffservState,'zyxelDiffservMapTable':zyxelDiffservMapTable,'zyxelDiffservMapEntry':zyxelDiffservMapEntry,_F:zyDiffservMapDscp,'zyDiffservMapPriority':zyDiffservMapPriority,'zyxelDiffservPortTable':zyxelDiffservPortTable,'zyxelDiffservPortEntry':zyxelDiffservPortEntry,'zyDiffservPortState':zyDiffservPortState})