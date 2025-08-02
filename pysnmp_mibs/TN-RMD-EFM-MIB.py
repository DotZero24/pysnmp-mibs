_I='read-write'
_H='read-only'
_G='tnSysSwitchId'
_F='TROPIC-SYSTEM-MIB'
_E='tnRmdSystemId'
_D='TN-RMD-SYSTEM-MIB'
_C='tnRmdIfIndex'
_B='TN-RMD-IF-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention','TruthValue')
tnRmdIfIndex,=mibBuilder.importSymbols(_B,_C)
tnRmdSystemId,=mibBuilder.importSymbols(_D,_E)
tnRmdMIBModules,tnRmdObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnRmdMIBModules','tnRmdObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_F,_G)
tnRmdEfmMibModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,4,2))
if mibBuilder.loadTexts:tnRmdEfmMibModule.setRevisions(('2018-02-23 12:00','2016-11-16 00:00','2012-11-28 00:00'))
class TnRmdSystemEfmDefect(TextualConvention,Bits):status=_A;namedValues=NamedValues(('lop',0))
_TnRmdEfmObjects_ObjectIdentity=ObjectIdentity
tnRmdEfmObjects=_TnRmdEfmObjects_ObjectIdentity((1,3,6,1,4,1,7483,6,4,1,2))
_TnRmdEfmAttributeTotal_Type=Integer32
_TnRmdEfmAttributeTotal_Object=MibScalar
tnRmdEfmAttributeTotal=_TnRmdEfmAttributeTotal_Object((1,3,6,1,4,1,7483,6,4,1,2,1),_TnRmdEfmAttributeTotal_Type())
tnRmdEfmAttributeTotal.setMaxAccess(_H)
if mibBuilder.loadTexts:tnRmdEfmAttributeTotal.setStatus(_A)
_TnRmdSystemEfmTable_Object=MibTable
tnRmdSystemEfmTable=_TnRmdSystemEfmTable_Object((1,3,6,1,4,1,7483,6,4,1,2,2))
if mibBuilder.loadTexts:tnRmdSystemEfmTable.setStatus(_A)
_TnRmdSystemEfmEntry_Object=MibTableRow
tnRmdSystemEfmEntry=_TnRmdSystemEfmEntry_Object((1,3,6,1,4,1,7483,6,4,1,2,2,1))
tnRmdSystemEfmEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_B,_C))
if mibBuilder.loadTexts:tnRmdSystemEfmEntry.setStatus(_A)
_TnRmdSystemEfmEnabled_Type=TruthValue
_TnRmdSystemEfmEnabled_Object=MibTableColumn
tnRmdSystemEfmEnabled=_TnRmdSystemEfmEnabled_Object((1,3,6,1,4,1,7483,6,4,1,2,2,1,1),_TnRmdSystemEfmEnabled_Type())
tnRmdSystemEfmEnabled.setMaxAccess(_I)
if mibBuilder.loadTexts:tnRmdSystemEfmEnabled.setStatus(_A)
_TnRmdSystemEfmDefect_Type=TnRmdSystemEfmDefect
_TnRmdSystemEfmDefect_Object=MibTableColumn
tnRmdSystemEfmDefect=_TnRmdSystemEfmDefect_Object((1,3,6,1,4,1,7483,6,4,1,2,2,1,2),_TnRmdSystemEfmDefect_Type())
tnRmdSystemEfmDefect.setMaxAccess(_H)
if mibBuilder.loadTexts:tnRmdSystemEfmDefect.setStatus(_A)
_TnRmdEfmCountersTable_Object=MibTable
tnRmdEfmCountersTable=_TnRmdEfmCountersTable_Object((1,3,6,1,4,1,7483,6,4,1,2,3))
if mibBuilder.loadTexts:tnRmdEfmCountersTable.setStatus(_A)
_TnRmdEfmCountersEntry_Object=MibTableRow
tnRmdEfmCountersEntry=_TnRmdEfmCountersEntry_Object((1,3,6,1,4,1,7483,6,4,1,2,3,1))
tnRmdEfmCountersEntry.setIndexNames((0,_F,_G),(0,_D,_E),(0,_B,_C))
if mibBuilder.loadTexts:tnRmdEfmCountersEntry.setStatus(_A)
_TnRmdEfmCountersRxNrNearEndErroredSymbols_Type=Counter64
_TnRmdEfmCountersRxNrNearEndErroredSymbols_Object=MibTableColumn
tnRmdEfmCountersRxNrNearEndErroredSymbols=_TnRmdEfmCountersRxNrNearEndErroredSymbols_Object((1,3,6,1,4,1,7483,6,4,1,2,3,1,1),_TnRmdEfmCountersRxNrNearEndErroredSymbols_Type())
tnRmdEfmCountersRxNrNearEndErroredSymbols.setMaxAccess(_H)
if mibBuilder.loadTexts:tnRmdEfmCountersRxNrNearEndErroredSymbols.setStatus(_A)
_TnRmdEfmCountersReset_Type=TruthValue
_TnRmdEfmCountersReset_Object=MibTableColumn
tnRmdEfmCountersReset=_TnRmdEfmCountersReset_Object((1,3,6,1,4,1,7483,6,4,1,2,3,1,2),_TnRmdEfmCountersReset_Type())
tnRmdEfmCountersReset.setMaxAccess(_I)
if mibBuilder.loadTexts:tnRmdEfmCountersReset.setStatus(_A)
mibBuilder.exportSymbols('TN-RMD-EFM-MIB',**{'TnRmdSystemEfmDefect':TnRmdSystemEfmDefect,'tnRmdEfmMibModule':tnRmdEfmMibModule,'tnRmdEfmObjects':tnRmdEfmObjects,'tnRmdEfmAttributeTotal':tnRmdEfmAttributeTotal,'tnRmdSystemEfmTable':tnRmdSystemEfmTable,'tnRmdSystemEfmEntry':tnRmdSystemEfmEntry,'tnRmdSystemEfmEnabled':tnRmdSystemEfmEnabled,'tnRmdSystemEfmDefect':tnRmdSystemEfmDefect,'tnRmdEfmCountersTable':tnRmdEfmCountersTable,'tnRmdEfmCountersEntry':tnRmdEfmCountersEntry,'tnRmdEfmCountersRxNrNearEndErroredSymbols':tnRmdEfmCountersRxNrNearEndErroredSymbols,'tnRmdEfmCountersReset':tnRmdEfmCountersReset})