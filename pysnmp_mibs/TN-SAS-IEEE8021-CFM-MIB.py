_F='tnDot1agCfmMepExtnEntry'
_E='TN-SAS-IEEE8021-CFM-MIB'
_D='read-create'
_C='TruthValue'
_B='Unsigned32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
dot1agCfmMepEntry,=mibBuilder.importSymbols('IEEE8021-CFM-MIB','dot1agCfmMepEntry')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks',_B,'iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention',_C)
tnSASModules,tnSASObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSASModules','tnSASObjs')
tnSASIEEE8021CfmMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,7,2,1,1,11))
if mibBuilder.loadTexts:tnSASIEEE8021CfmMIBModule.setRevisions(('2010-01-01 00:00',))
_TnSASDot1agMIBObjs_ObjectIdentity=ObjectIdentity
tnSASDot1agMIBObjs=_TnSASDot1agMIBObjs_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,11))
_TnSASDot1agCfmMep_ObjectIdentity=ObjectIdentity
tnSASDot1agCfmMep=_TnSASDot1agCfmMep_ObjectIdentity((1,3,6,1,4,1,7483,7,2,2,2,11,1))
_TnDot1agCfmMepExtnTable_Object=MibTable
tnDot1agCfmMepExtnTable=_TnDot1agCfmMepExtnTable_Object((1,3,6,1,4,1,7483,7,2,2,2,11,1,1))
if mibBuilder.loadTexts:tnDot1agCfmMepExtnTable.setStatus(_A)
_TnDot1agCfmMepExtnEntry_Object=MibTableRow
tnDot1agCfmMepExtnEntry=_TnDot1agCfmMepExtnEntry_Object((1,3,6,1,4,1,7483,7,2,2,2,11,1,1,1))
if mibBuilder.loadTexts:tnDot1agCfmMepExtnEntry.setStatus(_A)
class _TnDot1agCfmMepSendAisOnPortDown_Type(TruthValue):defaultValue=2
_TnDot1agCfmMepSendAisOnPortDown_Type.__name__=_C
_TnDot1agCfmMepSendAisOnPortDown_Object=MibTableColumn
tnDot1agCfmMepSendAisOnPortDown=_TnDot1agCfmMepSendAisOnPortDown_Object((1,3,6,1,4,1,7483,7,2,2,2,11,1,1,1,1),_TnDot1agCfmMepSendAisOnPortDown_Type())
tnDot1agCfmMepSendAisOnPortDown.setMaxAccess(_D)
if mibBuilder.loadTexts:tnDot1agCfmMepSendAisOnPortDown.setStatus(_A)
class _TnDot1agCfmMepControlSapTag_Type(Unsigned32):defaultValue=0;subtypeSpec=Unsigned32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,0),ValueRangeConstraint(512,768))
_TnDot1agCfmMepControlSapTag_Type.__name__=_B
_TnDot1agCfmMepControlSapTag_Object=MibTableColumn
tnDot1agCfmMepControlSapTag=_TnDot1agCfmMepControlSapTag_Object((1,3,6,1,4,1,7483,7,2,2,2,11,1,1,1,2),_TnDot1agCfmMepControlSapTag_Type())
tnDot1agCfmMepControlSapTag.setMaxAccess(_D)
if mibBuilder.loadTexts:tnDot1agCfmMepControlSapTag.setStatus(_A)
dot1agCfmMepEntry.registerAugmentions((_E,_F))
tnDot1agCfmMepExtnEntry.setIndexNames(*dot1agCfmMepEntry.getIndexNames())
mibBuilder.exportSymbols(_E,**{'tnSASIEEE8021CfmMIBModule':tnSASIEEE8021CfmMIBModule,'tnSASDot1agMIBObjs':tnSASDot1agMIBObjs,'tnSASDot1agCfmMep':tnSASDot1agCfmMep,'tnDot1agCfmMepExtnTable':tnDot1agCfmMepExtnTable,_F:tnDot1agCfmMepExtnEntry,'tnDot1agCfmMepSendAisOnPortDown':tnDot1agCfmMepSendAisOnPortDown,'tnDot1agCfmMepControlSapTag':tnDot1agCfmMepControlSapTag})