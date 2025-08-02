_E='tnEventAppIndex'
_D='TN-LOG-MIB'
_C='tnSysSwitchId'
_B='TROPIC-SYSTEM-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
TNamedItem,=mibBuilder.importSymbols('TN-TC-MIB','TNamedItem')
tnSRMIBModules,tnSRObjs=mibBuilder.importSymbols('TROPIC-GLOBAL-REG','tnSRMIBModules','tnSRObjs')
tnSysSwitchId,=mibBuilder.importSymbols(_B,_C)
tnSRLogMIBModule=ModuleIdentity((1,3,6,1,4,1,7483,5,1,3,12))
if mibBuilder.loadTexts:tnSRLogMIBModule.setRevisions(('2012-12-05 00:00','2009-02-28 00:00','2008-01-01 00:00','2007-01-01 00:00','2006-03-15 00:00','2005-01-24 00:00','2004-05-27 00:00','2004-01-15 00:00','2003-08-15 00:00','2003-01-20 00:00','2001-11-10 00:00'))
_TnSRLogObjs_ObjectIdentity=ObjectIdentity
tnSRLogObjs=_TnSRLogObjs_ObjectIdentity((1,3,6,1,4,1,7483,6,1,2,12))
_TnEventAppTable_Object=MibTable
tnEventAppTable=_TnEventAppTable_Object((1,3,6,1,4,1,7483,6,1,2,12,9))
if mibBuilder.loadTexts:tnEventAppTable.setStatus(_A)
_TnEventAppEntry_Object=MibTableRow
tnEventAppEntry=_TnEventAppEntry_Object((1,3,6,1,4,1,7483,6,1,2,12,9,1))
tnEventAppEntry.setIndexNames((0,_B,_C),(0,_D,_E))
if mibBuilder.loadTexts:tnEventAppEntry.setStatus(_A)
_TnEventAppIndex_Type=Unsigned32
_TnEventAppIndex_Object=MibTableColumn
tnEventAppIndex=_TnEventAppIndex_Object((1,3,6,1,4,1,7483,6,1,2,12,9,1,1),_TnEventAppIndex_Type())
tnEventAppIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:tnEventAppIndex.setStatus(_A)
_TnEventAppName_Type=TNamedItem
_TnEventAppName_Object=MibTableColumn
tnEventAppName=_TnEventAppName_Object((1,3,6,1,4,1,7483,6,1,2,12,9,1,2),_TnEventAppName_Type())
tnEventAppName.setMaxAccess('read-only')
if mibBuilder.loadTexts:tnEventAppName.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'tnSRLogMIBModule':tnSRLogMIBModule,'tnSRLogObjs':tnSRLogObjs,'tnEventAppTable':tnEventAppTable,'tnEventAppEntry':tnEventAppEntry,_E:tnEventAppIndex,'tnEventAppName':tnEventAppName})