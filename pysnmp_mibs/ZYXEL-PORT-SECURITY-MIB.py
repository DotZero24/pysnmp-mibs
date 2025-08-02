_H='not-accessible'
_G='zyPortSecurityVMLVID'
_F='zyPortSecurityVMLPort'
_E='dot1dBasePort'
_D='BRIDGE-MIB'
_C='ZYXEL-PORT-SECURITY-MIB'
_B='read-write'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1dBasePort,=mibBuilder.importSymbols(_D,_E)
EnabledStatus,=mibBuilder.importSymbols('P-BRIDGE-MIB','EnabledStatus')
PortList,=mibBuilder.importSymbols('Q-BRIDGE-MIB','PortList')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention')
esMgmt,=mibBuilder.importSymbols('ZYXEL-ES-SMI','esMgmt')
zyxelPortSecurity=ModuleIdentity((1,3,6,1,4,1,890,1,15,3,66))
_ZyxelPortSecuritySetup_ObjectIdentity=ObjectIdentity
zyxelPortSecuritySetup=_ZyxelPortSecuritySetup_ObjectIdentity((1,3,6,1,4,1,890,1,15,3,66,1))
_ZyPortSecurityState_Type=EnabledStatus
_ZyPortSecurityState_Object=MibScalar
zyPortSecurityState=_ZyPortSecurityState_Object((1,3,6,1,4,1,890,1,15,3,66,1,1),_ZyPortSecurityState_Type())
zyPortSecurityState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortSecurityState.setStatus(_A)
_ZyxelPortSecurityPortTable_Object=MibTable
zyxelPortSecurityPortTable=_ZyxelPortSecurityPortTable_Object((1,3,6,1,4,1,890,1,15,3,66,1,2))
if mibBuilder.loadTexts:zyxelPortSecurityPortTable.setStatus(_A)
_ZyxelPortSecurityPortEntry_Object=MibTableRow
zyxelPortSecurityPortEntry=_ZyxelPortSecurityPortEntry_Object((1,3,6,1,4,1,890,1,15,3,66,1,2,1))
zyxelPortSecurityPortEntry.setIndexNames((0,_D,_E))
if mibBuilder.loadTexts:zyxelPortSecurityPortEntry.setStatus(_A)
_ZyPortSecurityPortState_Type=EnabledStatus
_ZyPortSecurityPortState_Object=MibTableColumn
zyPortSecurityPortState=_ZyPortSecurityPortState_Object((1,3,6,1,4,1,890,1,15,3,66,1,2,1,1),_ZyPortSecurityPortState_Type())
zyPortSecurityPortState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortSecurityPortState.setStatus(_A)
_ZyPortSecurityPortLearnState_Type=EnabledStatus
_ZyPortSecurityPortLearnState_Object=MibTableColumn
zyPortSecurityPortLearnState=_ZyPortSecurityPortLearnState_Object((1,3,6,1,4,1,890,1,15,3,66,1,2,1,2),_ZyPortSecurityPortLearnState_Type())
zyPortSecurityPortLearnState.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortSecurityPortLearnState.setStatus(_A)
_ZyPortSecurityPortMacLimit_Type=Integer32
_ZyPortSecurityPortMacLimit_Object=MibTableColumn
zyPortSecurityPortMacLimit=_ZyPortSecurityPortMacLimit_Object((1,3,6,1,4,1,890,1,15,3,66,1,2,1,3),_ZyPortSecurityPortMacLimit_Type())
zyPortSecurityPortMacLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortSecurityPortMacLimit.setStatus(_A)
_ZyPortSecurityMacFreeze_Type=PortList
_ZyPortSecurityMacFreeze_Object=MibScalar
zyPortSecurityMacFreeze=_ZyPortSecurityMacFreeze_Object((1,3,6,1,4,1,890,1,15,3,66,1,3),_ZyPortSecurityMacFreeze_Type())
zyPortSecurityMacFreeze.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortSecurityMacFreeze.setStatus(_A)
_ZyPortSecurityMaxNumberOfVMLs_Type=Integer32
_ZyPortSecurityMaxNumberOfVMLs_Object=MibScalar
zyPortSecurityMaxNumberOfVMLs=_ZyPortSecurityMaxNumberOfVMLs_Object((1,3,6,1,4,1,890,1,15,3,66,1,4),_ZyPortSecurityMaxNumberOfVMLs_Type())
zyPortSecurityMaxNumberOfVMLs.setMaxAccess('read-only')
if mibBuilder.loadTexts:zyPortSecurityMaxNumberOfVMLs.setStatus(_A)
_ZyxelPortSecurityVMLTable_Object=MibTable
zyxelPortSecurityVMLTable=_ZyxelPortSecurityVMLTable_Object((1,3,6,1,4,1,890,1,15,3,66,1,5))
if mibBuilder.loadTexts:zyxelPortSecurityVMLTable.setStatus(_A)
_ZyxelPortSecurityVMLEntry_Object=MibTableRow
zyxelPortSecurityVMLEntry=_ZyxelPortSecurityVMLEntry_Object((1,3,6,1,4,1,890,1,15,3,66,1,5,1))
zyxelPortSecurityVMLEntry.setIndexNames((0,_C,_F),(0,_C,_G))
if mibBuilder.loadTexts:zyxelPortSecurityVMLEntry.setStatus(_A)
_ZyPortSecurityVMLPort_Type=Integer32
_ZyPortSecurityVMLPort_Object=MibTableColumn
zyPortSecurityVMLPort=_ZyPortSecurityVMLPort_Object((1,3,6,1,4,1,890,1,15,3,66,1,5,1,1),_ZyPortSecurityVMLPort_Type())
zyPortSecurityVMLPort.setMaxAccess(_H)
if mibBuilder.loadTexts:zyPortSecurityVMLPort.setStatus(_A)
_ZyPortSecurityVMLVID_Type=Integer32
_ZyPortSecurityVMLVID_Object=MibTableColumn
zyPortSecurityVMLVID=_ZyPortSecurityVMLVID_Object((1,3,6,1,4,1,890,1,15,3,66,1,5,1,2),_ZyPortSecurityVMLVID_Type())
zyPortSecurityVMLVID.setMaxAccess(_H)
if mibBuilder.loadTexts:zyPortSecurityVMLVID.setStatus(_A)
_ZyPortSecurityVMLMacLimit_Type=Integer32
_ZyPortSecurityVMLMacLimit_Object=MibTableColumn
zyPortSecurityVMLMacLimit=_ZyPortSecurityVMLMacLimit_Object((1,3,6,1,4,1,890,1,15,3,66,1,5,1,3),_ZyPortSecurityVMLMacLimit_Type())
zyPortSecurityVMLMacLimit.setMaxAccess(_B)
if mibBuilder.loadTexts:zyPortSecurityVMLMacLimit.setStatus(_A)
_ZyPortSecurityVMLRowStatus_Type=RowStatus
_ZyPortSecurityVMLRowStatus_Object=MibTableColumn
zyPortSecurityVMLRowStatus=_ZyPortSecurityVMLRowStatus_Object((1,3,6,1,4,1,890,1,15,3,66,1,5,1,4),_ZyPortSecurityVMLRowStatus_Type())
zyPortSecurityVMLRowStatus.setMaxAccess('read-create')
if mibBuilder.loadTexts:zyPortSecurityVMLRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'zyxelPortSecurity':zyxelPortSecurity,'zyxelPortSecuritySetup':zyxelPortSecuritySetup,'zyPortSecurityState':zyPortSecurityState,'zyxelPortSecurityPortTable':zyxelPortSecurityPortTable,'zyxelPortSecurityPortEntry':zyxelPortSecurityPortEntry,'zyPortSecurityPortState':zyPortSecurityPortState,'zyPortSecurityPortLearnState':zyPortSecurityPortLearnState,'zyPortSecurityPortMacLimit':zyPortSecurityPortMacLimit,'zyPortSecurityMacFreeze':zyPortSecurityMacFreeze,'zyPortSecurityMaxNumberOfVMLs':zyPortSecurityMaxNumberOfVMLs,'zyxelPortSecurityVMLTable':zyxelPortSecurityVMLTable,'zyxelPortSecurityVMLEntry':zyxelPortSecurityVMLEntry,_F:zyPortSecurityVMLPort,_G:zyPortSecurityVMLVID,'zyPortSecurityVMLMacLimit':zyPortSecurityVMLMacLimit,'zyPortSecurityVMLRowStatus':zyPortSecurityVMLRowStatus})