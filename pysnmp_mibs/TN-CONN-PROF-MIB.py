_H='TnConnProfVlanRanges'
_G='tnConnProfId'
_F='TN-CONN-PROF-MIB'
_E='tnSysSwitchId'
_D='TROPIC-SYSTEM-MIB'
_C='TItemDescription'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TimeStamp=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TimeStamp')
TItemDescription,TmnxEncapVal=mibBuilder.importSymbols('TN-TC-MIB',_C,'TmnxEncapVal')
tnSRMIBModules,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_D,_E)
tnConnProfMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,75))
if mibBuilder.loadTexts:tnConnProfMIBModule.setRevisions(('2019-10-18 00:00','2015-04-06 00:00','2011-02-01 00:00'))
class TnConnProfId(TextualConvention,Unsigned32):status=_A;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(1,1000))
class TnConnProfVlanRanges(DisplayString):status=_A;subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,512))
_TnConnProfObjs_ObjectIdentity=ObjectIdentity
tnConnProfObjs=_TnConnProfObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,75))
_TnConnProfConfigObjs_ObjectIdentity=ObjectIdentity
tnConnProfConfigObjs=_TnConnProfConfigObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,75,2))
_TnConnProfTable_Object=MibTable
tnConnProfTable=_TnConnProfTable_Object((1,3,6,1,4,1,7483,6,1,2,75,2,1))
if mibBuilder.loadTexts:tnConnProfTable.setStatus(_A)
_TnConnProfEntry_Object=MibTableRow
tnConnProfEntry=_TnConnProfEntry_Object((1,3,6,1,4,1,7483,6,1,2,75,2,1,1))
tnConnProfEntry.setIndexNames((0,_D,_E),(0,_F,_G))
if mibBuilder.loadTexts:tnConnProfEntry.setStatus(_A)
_TnConnProfId_Type=TnConnProfId
_TnConnProfId_Object=MibTableColumn
tnConnProfId=_TnConnProfId_Object((1,3,6,1,4,1,7483,6,1,2,75,2,1,1,1),_TnConnProfId_Type())
tnConnProfId.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnConnProfId.setStatus(_A)
_TnConnProfRowStatus_Type=RowStatus
_TnConnProfRowStatus_Object=MibTableColumn
tnConnProfRowStatus=_TnConnProfRowStatus_Object((1,3,6,1,4,1,7483,6,1,2,75,2,1,1,2),_TnConnProfRowStatus_Type())
tnConnProfRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:tnConnProfRowStatus.setStatus(_A)
_TnConnProfLastChanged_Type=TimeStamp
_TnConnProfLastChanged_Object=MibTableColumn
tnConnProfLastChanged=_TnConnProfLastChanged_Object((1,3,6,1,4,1,7483,6,1,2,75,2,1,1,3),_TnConnProfLastChanged_Type())
tnConnProfLastChanged.setMaxAccess('read-only')
if mibBuilder.loadTexts:tnConnProfLastChanged.setStatus(_A)
class _TnConnProfDescription_Type(TItemDescription):defaultValue=OctetString('')
_TnConnProfDescription_Type.__name__=_C
_TnConnProfDescription_Object=MibTableColumn
tnConnProfDescription=_TnConnProfDescription_Object((1,3,6,1,4,1,7483,6,1,2,75,2,1,1,4),_TnConnProfDescription_Type())
tnConnProfDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:tnConnProfDescription.setStatus(_A)
class _TnConnProfVlanRange_Type(TnConnProfVlanRanges):defaultValue=OctetString('')
_TnConnProfVlanRange_Type.__name__=_H
_TnConnProfVlanRange_Object=MibTableColumn
tnConnProfVlanRange=_TnConnProfVlanRange_Object((1,3,6,1,4,1,7483,6,1,2,75,2,1,1,5),_TnConnProfVlanRange_Type())
tnConnProfVlanRange.setMaxAccess(_B)
if mibBuilder.loadTexts:tnConnProfVlanRange.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'TnConnProfId':TnConnProfId,_H:TnConnProfVlanRanges,'tnConnProfMIBModule':tnConnProfMIBModule,'tnConnProfObjs':tnConnProfObjs,'tnConnProfConfigObjs':tnConnProfConfigObjs,'tnConnProfTable':tnConnProfTable,'tnConnProfEntry':tnConnProfEntry,_G:tnConnProfId,'tnConnProfRowStatus':tnConnProfRowStatus,'tnConnProfLastChanged':tnConnProfLastChanged,'tnConnProfDescription':tnConnProfDescription,'tnConnProfVlanRange':tnConnProfVlanRange})